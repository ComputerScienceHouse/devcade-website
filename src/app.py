import flask
from werkzeug.utils import secure_filename
from flask_login import login_required, current_user
from auth import app
import requests

@app.route('/')
# @login_required
def homepage():
    return flask.render_template('home.html')

@app.route('/about')
def aboutpage():
    return flask.render_template('about.html')

@app.route('/catalog')
def catalogpage():
    games = requests.get(app.config["DEVCADE_API_URI"] + "games/gamelist").json()
    return flask.render_template('catalog.html', gamelist=games)

@app.route('/user')
def user():
    return "<p>not implemented</p>"
    if not current_user.is_authenticated:
        return flask.redirect('/login')
    return flask.render_template('profile.html', savelist=saves[current_user.id])

@app.route('/game/<id>')
def getgame(id):
    games = requests.get(app.config["DEVCADE_API_URI"] + "games/gamelist").json()
    for i in range(len(games)):
        if games[i]['id'] == id:
            break
    else:
        flask.render_template('404.html')
    return flask.render_template('game.html', game=i, gamelist=games)

@app.route('/upload_game', methods = ['POST'])
@login_required
def uploadgame():
    if flask.request.method == 'POST':
        f = flask.request.files['file']
        title = flask.request.args.get('title')
        files = {'file': f.stream}
        values = {'title': title}
        r = requests.post(app.config["DEVCADE_API_URI"] + "games/upload", files=files, data=values)
        return "<p>" + r.text + "</p>"

@app.route('/upload')
@login_required
def uploadpage():
    games = requests.get(app.config["DEVCADE_API_URI"] + "games/gamelist").json()
    usergames = []
    for i in games:
        if i['author'] == current_user.id:
            usergames.append(i)
    return flask.render_template('upload.html', title='Devcade - Upload', gamelist=usergames)

@app.errorhandler(Exception)
def page404(e):
    eCode = 500
    message = "An unknown error occured!"
    try:
        message = e.description
        eCode = e.code
    finally:
        return flask.render_template('error.html', error=eCode, message=message)

if __name__ == '__main__':
    app.run(host='localhost', debug=True)
