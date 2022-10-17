import flask
from flask_login import login_required, current_user
from auth import app

guest = {
    'name': 'Guest',
    'username': 'Guest',
    'img': './static/images/guest.png',
    'admin': False
}

@app.route('/')
# @login_required
def homepage():
    return flask.render_template('home.html', user=guest)

@app.route('/about')
def aboutpage():
    return flask.render_template('about.html', user=guest)

@app.route('/catalog')
def catalogpage():
    return flask.render_template('catalog.html', user=guest)

@app.route('/upload')
def uploadpage():
    return flask.render_template('upload.html', user=guest)

if __name__ == '__main__':
    app.run(host='localhost')
