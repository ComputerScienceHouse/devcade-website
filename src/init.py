import os
import pytz
import flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_pyoidc.flask_pyoidc import OIDCAuthentication
from flask_pyoidc.provider_configuration import ProviderConfiguration, ClientMetadata
from urllib.parse import quote_plus


app = flask.Flask(__name__)
app.jinja_env.filters['quote_plus'] = lambda u: quote_plus(u)
try:
    app.config.from_pyfile(os.path.join(os.getcwd(), "config.py"))
except:
    app.config.from_pyfile("config.py")

# time setup for the server side time
eastern = pytz.timezone('America/New_York')

# OIDC Authentication
CSH_AUTH = ProviderConfiguration(issuer=app.config["OIDC_ISSUER"],
                                 client_metadata=ClientMetadata(
                                     app.config["OIDC_CLIENT_ID"],
                                     app.config["OIDC_CLIENT_SECRET"]))
GOOGLE_AUTH = ProviderConfiguration(issuer=app.config["GOOGLE_OIDC_ISSUER"],
                                 client_metadata=ClientMetadata(
                                     app.config["GOOGLE_OIDC_CLIENT_ID"],
                                     app.config["GOOGLE_OIDC_CLIENT_SECRET"]),
                                 auth_request_params={'scope': ['email', 'profile', 'openid']})
auth = OIDCAuthentication(
    {
        'default': CSH_AUTH,
        'google': GOOGLE_AUTH
    },
    app
)

auth.init_app(app)
app.secret_key = app.config["SECRET_KEY"] # os.urandom(16)
