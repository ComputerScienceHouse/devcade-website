import flask
from werkzeug.utils import secure_filename
from flask_login import login_required, current_user
from auth import app
import config

games = [
    {
        "title":"Flappy Meatball",
        "id":"flappy-meatball",
        "desc":"Flappy Bird is a mobile game developed by Vietnamese video game artist and programmer Dong Nguyen, under his game development company .Gears. The game is a side-scroller where the player controls a bird, attempting to fly between columns of green pipes without hitting them. Nguyen created the game over the period of several days, using a bird protagonist that he had designed for a cancelled game in 2012.",
        "author":"andrewe",

    }, {
        "title":"Brickbreaker",
        "id":"brickbreakder",
        "desc":"Brick Breaker is a video game, which was developed by Ali Asaria,[1] that came preloaded on the BlackBerry and is now available on App Store (iOS). ",
        "author":"ella"
    } ,{
        "title":"Pong",
        "id":"pong",
        "desc":"Pong is a table tennis–themed twitch arcade sports video game, featuring simple two-dimensional graphics, manufactured by Atari and originally released in 1972. It was one of the earliest arcade video games; it was created by Allan Alcorn as a training exercise assigned to him by Atari co-founder Nolan Bushnell, but Bushnell and Atari co-founder Ted Dabney were surprised by the quality of Alcorn's work and decided to manufacture the game. Bushnell based the game's concept on an electronic ping-pong game included in the Magnavox Odyssey, the first home video game console. In response, Magnavox later sued Atari for patent infringement. ",
        "author":"lyons"
    },{
        "title":"Spacewar!",
        "id":"spacewar",
        "desc":"Spacewar! is a space combat video game developed in 1962 by Steve Russell in collaboration with Martin Graetz, Wayne Wiitanen, Bob Saunders, Steve Piner, and others. It was written for the newly installed DEC PDP-1 minicomputer at the Massachusetts Institute of Technology. After its initial creation, Spacewar! was expanded further by other students and employees of universities in the area, including Dan Edwards and Peter Samson. It was also spread to many of the few dozen installations of the PDP-1 computer, making Spacewar! the first known video game to be played at multiple computer installations. ",
        "author":"mcdade"
    },{
        "title":"Minecraft",
        "id":"minecraft",
        "desc":"Minecraft is a sandbox video game developed by Mojang Studios. The game was created by Markus 'Notch' Persson in the Java programming language. Following several early private testing versions, it was first made public in May 2009 before being fully released in November 2011, with Notch stepping down and Jens 'Jeb' Bergensten taking over development. Minecraft has since been ported to several other platforms and is the best-selling video game of all time, with over 238 million copies sold and nearly 140 million monthly active players as of 2021. ",
        "author":"notch"
    }
]

saves = {
    "mcdade" : [
    {
        "title": "Brickbreaker",
        "highscore":None
    }, {
        "title": "Spacewar!",
        "highscore":None
    }, {
        "title": "Minecraft",
        "highscore": 350
    }],
    "cinnamon" : [
    {
        "title": "Brickbreaker",
        "highscore": 200
    }, {
        "title": "Spacewar!",
        "highscore": 63
    }, {
        "title": "Minecraft",
        "highscore": None
    }]
}

@app.route('/')
# @login_required
def homepage():
    return flask.render_template('home.html')

@app.route('/about')
def aboutpage():
    return flask.render_template('about.html')

@app.route('/catalog')
def catalogpage():
    return flask.render_template('catalog.html', gamelist=games)

@app.route('/user')
def user():
    if not current_user.is_authenticated:
        return flask.redirect('/login')
    return flask.redirect('/user/' + current_user.id)

@app.route('/user/<uname>')
def userprofile(uname):
    return flask.render_template('profile.html', savelist=saves[uname])

@app.route('/game/<id>')
def getgame(id):
    for i in range(len(games)):
        if games[i]['id'] == id:
            break
    else:
        flask.render_template('404.html')
    return flask.render_template('game.html', game=i, gamelist=games)

@app.route('/upload_game', methods = ['POST'])
def uploadgame():
    if flask.request.method == 'POST':
        f = flask.request.files['file']
        f.save(secure_filename(f.filename))
        return '', 204

@app.route('/upload')
def uploadpage():
    if not current_user.is_authenticated:
        return flask.redirect('/login')
    return flask.render_template('upload.html', title='Devcade - Upload', gamelist=games)

def upload(file, key):

    bucket = s3.Bucket('devcade-games')

    bucket.upload_file(Filename=file,
                       Key=key)

if __name__ == '__main__':
    app.run(host='localhost', debug=True)
