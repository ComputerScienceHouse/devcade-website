from init import app, auth
from models import User
from flask_login import login_user, logout_user, LoginManager
import flask
import requests
import sys

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
            "user_type": "CSH",
            "first": first,
            "last": last,
            "email": f"{uid}@csh.rit.edu",
            "picture": picture,
            "admin": any(is_eboard, is_rtp, is_devcade_admin)
        }
        kwargs["auth_dict"] = auth_dict
        return func(*args, **kwargs)
    return wrapped_function

def google_user_auth(func):
    @wraps(func)
    def wrapped_function(*args, **kwargs):
        uid = str(flask.session["userinfo"].get("sub", ""))
        last = str(flask.session["userinfo"].get("family_name", ""))
        first = str(flask.session["userinfo"].get("given_name", ""))
        email = str(flask.session["userinfo"].get("email", ""))
        picture = str(flask.session["userinfo"].get("picture", ""))
        auth_dict = {
            "uid": uid,
            "user_type": "GOOGLE",
            "first": first,
            "last": last,
            "email": email,
            "picture": picture,
            "admin": False
        }
        kwargs["auth_dict"] = auth_dict
        return func(*args, **kwargs)
    return wrapped_function

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'homepage'

@login_manager.user_loader
def load_user(user_id):
    user_req = requests.get(app.config["DEVCADE_API_URI"] + "users/" + user_id)
    if user_req.status_code == 200:
        user_data = user_req.json()
        user = User(user_data['id'], user_data['user_type'], user_data['first_name'], user_data['last_name'], user_data['email'], user_data['picture'], user_data['admin'])
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
    """
    Gets new logger inner data
    """
    if auth_dict is None:
        return flask.redirect("/csh_auth")
    return update_backend_user(auth_dict)

@app.route('/google_auth')
@auth.oidc_auth('google')
@google_user_auth
def google_auth(auth_dict=None):
    """
    Gets new logger inner data
    """
    if auth_dict is None:
        return flask.redirect("/google_auth")
    return update_backend_user(auth_dict)


def update_backend_user(auth_dict):
    # headers={"frontend_api_key":app.config["FRONTEND_API_KEY"]}
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
        }, headers={"frontend_api_key":app.config["FRONTEND_API_KEY"]})
    else:
        requests.put(app.config["DEVCADE_API_URI"] + "users/" + auth_dict['uid'], json={
            'id': auth_dict['uid'],
            'user_type': auth_dict['user_type'],
            'first_name': auth_dict['first'],
            'last_name': auth_dict['last'],
            'picture': auth_dict['picture'],
            'email': auth_dict['email'],
            'admin': auth_dict['admin']
        }, headers={"frontend_api_key":app.config["FRONTEND_API_KEY"]})
    login_user(User(auth_dict['uid'], auth_dict['user_type'], auth_dict['first'], auth_dict['last'], auth_dict['email'], auth_dict['picture'], auth_dict['admin']))
    goto = flask.request.args.get('goto')
    if goto == None:
        goto = 'homepage'
    try:
        goto = flask.url_for(goto)
    except:
        goto = flask.url_for('homepage')
    return flask.redirect(goto)
