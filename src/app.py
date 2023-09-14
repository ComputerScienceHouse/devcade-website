import flask
from werkzeug.utils import secure_filename
from flask_login import login_required, current_user
from auth import app
import requests
from io import BytesIO
from werkzeug.wsgi import FileWrapper 
import json
import hashlib

contributors = json.load(open("./static/json/contributors.json", "r"))
for year in contributors:
    for person in contributors[year]:
        person['emailHash'] = hashlib.md5(str.encode(person['email'])).hexdigest()

@app.route('/')
# @login_required
def homepage():
    return flask.render_template('home.html')

@app.route('/catalog')
def catalogpage():
    tag = flask.request.args.get("tag")
    games = requests.get(app.config["DEVCADE_API_URI"] + "games/").json()
    if tag:
        games = list(filter(lambda g: tag in map(lambda t: t['name'], g['tags']), games))
    return flask.render_template('catalog.html', gamelist=games)

@app.route('/user')
def user():
    return "<p>not implemented</p>"
    if not current_user.is_authenticated:
        return flask.redirect('/login')
    return flask.render_template('profile.html', savelist=saves[current_user.id])

@app.route('/game/<id>')
def getgame(id):
    game_req = requests.get(app.config["DEVCADE_API_URI"] + f"games/{id}")
    if game_req.status_code == 404:
        flask.render_template('404.html')
    return flask.render_template('game.html', game=game_req.json())

@app.route('/upload_game', methods = ['POST'])
@login_required
def uploadgame():
    if flask.request.method == 'POST':
        game = flask.request.files['game']
        banner = flask.request.files['banner']
        icon = flask.request.files['icon']
        title = flask.request.form['title']
        description = flask.request.form['description']
        tags = flask.request.form['tags']
        author = current_user.id
        file = {
            'game': ("game.zip", game.stream, "application/zip"),
            'banner': ("banner", banner.stream, banner.mimetype),
            'icon': ("icon", icon.stream, icon.mimetype)
        }
        fields = {'title': title, 'description': description, 'author': author, 'tags': tags}
        r = requests.post(app.config["DEVCADE_API_URI"] + "games/", files=file, data=fields, headers={"frontend_api_key":app.config["FRONTEND_API_KEY"]})
        if r.status_code == 201:
            return flask.redirect('/catalog')
        return "<p>" + r.text + "</p>"

@app.route('/upload')
@login_required
def uploadpage():
    usergames = []
    try:
        games = requests.get(app.config["DEVCADE_API_URI"] + "games/").json()
        tags = requests.get(app.config["DEVCADE_API_URI"] + "tags/").json()
        for i in games:
            if i['author'] == current_user.id:
                usergames.append(i)
    except(Exception):
        print("api offline")
    return flask.render_template('upload.html', title='Devcade - Upload', gamelist=usergames, tags=tags)

@app.route('/download/<id>')
def download(id):
    r = requests.get(app.config["DEVCADE_API_URI"] + f"games/{id}/game", stream=True)
    b = BytesIO(r.content)
    game = FileWrapper(b)
    return flask.Response(game, mimetype="application/zip", direct_passthrough=True)

@app.route('/admin/delete/<id>')
@login_required
def deleteGame(id):
    game = requests.get(app.config['DEVCADE_API_URI'] + "games/" + id).json()
    author = game['author']
    if(current_user.admin or current_user.id == author):
        r = requests.delete(app.config["DEVCADE_API_URI"] + "games/" + id, headers={"frontend_api_key":app.config["FRONTEND_API_KEY"]})
        if r.status_code != 200:
            return r.text
    else:
        return "<p>Stop hacking</p>"
    return flask.redirect('/catalog')

@app.route("/sitemap.xml")
@app.route("/robots.txt")
@app.route("/favicon.ico")
def static_from_root():
    return flask.send_from_directory(app.static_folder, flask.request.path[1:])

@app.route('/credits')
def credits():
    return flask.render_template('credits.html', contributors = contributors, last_year=list(contributors.keys())[0])

@app.route('/gamejam')
def gamejam():
    return flask.render_template('gamejam.html')

@app.route('/preseed')
def preseed():
    return flask.redirect('https://raw.githubusercontent.com/ComputerScienceHouse/Devcade-onboard/main/dcu/preseed.txt')

@app.route('/docs')
def docs():
    return flask.redirect('https://devcade-docs.csh.rit.edu')


@app.errorhandler(Exception)
def page404(e):
    eCode = 500
    message = "An unknown error occured!"
    try:
        app.log_exception(e)
        message = e.description
        eCode = e.code
    finally:
        return flask.render_template('error.html', error=eCode, message=message), eCode

if __name__ == '__main__':
    app.run(host='localhost', debug=True)
