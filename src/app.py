import flask
from flask_login import login_required, current_user
from auth import app

@app.route('/')
# @login_required
def homepage():
    return flask.render_template('home.html')

@app.route('/about')
def aboutpage():
    return flask.render_template('about.html')

@app.route('/catalog')
def catalogpage():
    return flask.render_template('catalog.html')

@app.route('/upload')
def uploadpage():
    return flask.render_template('upload.html', title='Devcade - Upload')

if __name__ == '__main__':
    app.run(host='localhost')
