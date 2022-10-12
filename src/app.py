import flask
from flask_login import login_required, current_user
from auth import app

@app.route('/')
# @login_required
def homepage():
    return flask.render_template('home.html')

if __name__ == '__main__':
    app.run()
