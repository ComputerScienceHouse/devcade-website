from init import app, auth, db
from models import Users
from flask_login import login_user, logout_user, LoginManager
import flask

from functools import wraps


def csh_user_auth(func):
    @wraps(func)
    def wrapped_function(*args, **kwargs):
        uid = str(flask.session["userinfo"].get("preferred_username", ""))
        last = str(flask.session["userinfo"].get("family_name", ""))
        first = str(flask.session["userinfo"].get("given_name", ""))
        picture = "https://profiles.csh.rit.edu/image/" + uid
        groups = flask.session["userinfo"].get("groups", [])
        is_eboard = "eboard" in groups
        is_rtp = "rtp" in groups
        is_devcade_admin = "devcade" in groups
        auth_dict = {
            "uid": uid,
            "first": first,
            "last": last,
            "picture": picture,
            "admin": is_eboard or is_rtp or is_devcade_admin
        }
        kwargs["auth_dict"] = auth_dict
        return func(*args, **kwargs)
    return wrapped_function

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'csh_auth'


@login_manager.user_loader
def load_user(user_id):
    q = Users.query.get(user_id)
    if q:
        return q
    return None


@app.route("/logout")
@auth.oidc_logout
def _logout():
    logout_user()
    return flask.redirect("/", 302)


@app.route('/csh_auth')
@app.route('/login')
@auth.oidc_auth('default')
@csh_user_auth
def csh_auth(auth_dict=None):
    """
    Gets new logger inner data
    """
    if auth_dict is None:
        return flask.redirect("/csh_auth")
    user = Users.query.get(auth_dict['uid'])
    if user is not None:
        user.firstname = auth_dict['first']
        user.lastname = auth_dict['last']
        user.picture = auth_dict['picture']
        user.admin = auth_dict['admin']
    else:
        user = Users(auth_dict['uid'], auth_dict['first'],
                    auth_dict['last'], auth_dict['picture'], auth_dict['admin'])
        db.session.add(user)
    db.session.commit()
    login_user(user)
    goto = flask.request.args.get('goto')
    if goto == None:
        goto = 'homepage'
    try:
        goto = flask.url_for(goto)
    except:
        goto = flask.url_for('homepage')
    return flask.redirect(goto)


with app.app_context():
        db.create_all()