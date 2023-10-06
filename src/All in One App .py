import os
import pytz
import flask
import requests
from functools import wraps
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_pyoidc.flask_pyoidc import OIDCAuthentication
from flask_pyoidc.provider_configuration import ProviderConfiguration, ClientMetadata
from urllib.parse import quote_plus
from flask_login import login_user, logout_user, LoginManager

app = flask.Flask(__name__)
app.jinja_env.filters['quote_plus'] = lambda u: quote_plus(u

# Flask configuration
app.config.update(
    SECRET_KEY=os.urandom(16),
    IP=os.environ.get('IP', '0.0.0.0'),
    PORT=os.environ.get('PORT', 8080),
    SERVER_NAME=os.environ.get('SERVER_NAME', 'localhost:5000'),
    PREFERRED_URL_SCHEME=os.environ.get('PREFERRED_URL_SCHEME', 'https'),
    POSTGRESQL_USER=os.environ.get('POSTGRESQL_USER', ''),
    POSTGRESQL_PASSWORD=os.environ.get('POSTGRESQL_PASSWORD'),
    POSTGRESQL_DATABASE=os.environ.get('POSTGRESQL_DATABASE', 'usersDB'),
    POSTGRESQL_IP=os.environ.get('POSTGRESQL_IP'),
    SQLALCHEMY_DATABASE_URI=os.environ.get(
        'SQLALCHEMY_DATABASE_URI',
        f"postgresql://{os.environ.get('POSTGRESQL_USER', '')}:{os.environ.get('POSTGRESQL_PASSWORD')}@"
        f"{os.environ.get('POSTGRESQL_IP')}/{os.environ.get('POSTGRESQL_DATABASE', 'usersDB')}"
    ) if os.environ.get('POSTGRESQL_USER', '') else 'sqlite:///users.sqlite3',
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
    OIDC_ISSUER=os.environ.get('OIDC_ISSUER', 'https://sso.csh.rit.edu/auth/realms/csh'),
    OIDC_CLIENT_ID=os.environ.get('OIDC_CLIENT_ID', 'devcade'),
    OIDC_CLIENT_SECRET=os.environ.get('OIDC_CLIENT_SECRET', 'NOT-A-SECRET'),
    GOOGLE_OIDC_ISSUER=os.environ.get('GOOGLE_OIDC_ISSUER', 'https://sso.csh.rit.edu/auth/realms/csh'),
    GOOGLE_OIDC_CLIENT_ID=os.environ.get('GOOGLE_OIDC_CLIENT_ID', 'devcade'),
    GOOGLE_OIDC_CLIENT_SECRET=os.environ.get('GOOGLE_OIDC_CLIENT_SECRET', 'NOT-A-SECRET'),
    DEVCADE_API_URI=os.environ.get('DEVCADE_API_URI'),
    FRONTEND_API_KEY=os.environ.get('FRONTEND_API_KEY'),
    DEVCADE_IS_DEV=os.environ.get('DEVCADE_IS_DEV')
)

# Time setup for the server-side time
eastern = pytz.timezone('America/New_York')

# OIDC Authentication
CSH_AUTH = ProviderConfiguration(
    issuer=app.config["OIDC_ISSUER"],
    client_metadata=ClientMetadata(
        app.config["OIDC_CLIENT_ID"],
        app.config["OIDC_CLIENT_SECRET"]
    )
)

GOOGLE_AUTH = ProviderConfiguration(
    issuer=app.config["GOOGLE_OIDC_ISSUER"],
    client_metadata=ClientMetadata(
        app.config["GOOGLE_OIDC_CLIENT_ID"],
        app.config["GOOGLE_OIDC_CLIENT_SECRET"]
    ),
    auth_request_params={'scope': ['email', 'profile', 'openid']}
)

auth = OIDCAuthentication(
    {
        'default': CSH_AUTH,
        'google': GOOGLE_AUTH
    },
    app
)

auth.init_app(app)

# Create a SQLAlchemy database instance
db = SQLAlchemy(app)

# Create Flask-Migrate instance
migrate = Migrate(app, db)

# Create a LoginManager instance
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'homepage'

@login_manager.user_loader
def load_user(user_id):
    user_req = requests.get(app.config["DEVCADE_API_URI"] + "users/" + user_id)
    if user_req.status_code == 200:
        user_data = user_req.json()
        user = User(user_data['id'], user_data['user_type'], user_data['first_name'], user_data['last_name'],
                    user_data['email'], user_data['picture'], user_data['admin'])
        return user
    return None

@app.route("/logout")
@auth.oidc_logout
def _logout():
    logout_user()
    return flask.redirect("/", 302)

@app.route('/csh_auth')
@auth.oidc_auth('default')
@csh_user_auth
def csh_auth(auth_dict=None):
    if auth_dict is None:
        return flask.redirect("/csh_auth")
    return update_backend_user(auth_dict)

@app.route('/google_auth')
@auth.oidc_auth('google')
@google_user_auth
def google_auth(auth_dict=None):
    if auth_dict is None:
        return flask.redirect("/google_auth")
    return update_backend_user(auth_dict)

def update_backend_user(auth_dict):
    user_req = requests.get(app.config["DEVCADE_API_URI"] + "users/" + auth_dict['uid'])
    if user_req.status_code == 400:
        requests.post(app.config["DEVCADE_API_URI"] + "users/", json={
            'id': auth_dict['uid'],
            'user_type': auth_dict['user_type'],
            'first_name': auth_dict['first'],
            'last_name': auth_dict['last'],
            'picture': auth_dict['picture'],
            'email': auth_dict['email'],
            'admin': auth_dict['admin']
        }, headers={"frontend_api_key": app.config["FRONTEND_API_KEY"]})
    else:
        requests.put(app.config["DEVCADE_API_URI"] + "users/" + auth_dict['uid'], json={
            'id': auth_dict['uid'],
            'user_type': auth_dict['user_type'],
            'first_name': auth_dict['first'],
            'last_name': auth_dict['last'],
            'picture': auth_dict['picture'],
            'email': auth_dict['email'],
            'admin': auth_dict['admin']
        }, headers={"frontend_api_key": app.config["FRONTEND_API_KEY"]})
    login_user(User(auth_dict['uid'], auth_dict['user_type'], auth_dict['first'], auth_dict['last'], auth_dict['email'], auth_dict['picture'], auth_dict['admin']))
    goto = flask.request.args.get('goto')
    if goto == None:
        goto = 'homepage'
    try:
        goto = flask.url_for(goto)
    except:
        goto = flask.url_for('homepage')
    return flask.redirect(goto)

# Rest of your code, including the User class and other routes...

if __name__ == "__main__":
    app.run(host=app.config['IP'], port=app.config['PORT'])
