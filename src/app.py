import flask
from flask_login import login_required, current_user
from auth import app

@app.route('/')
# @login_required
def get_in():
    return flask.render_template('home.html')


