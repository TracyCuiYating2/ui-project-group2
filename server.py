from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
from itsdangerous import json
app = Flask(__name__)

learnData = {
    "1": {
        "id": 1,
        "chord": "G",
        "chordIMG": "https://b7d3d5f9.rocketcdn.me/chords/standard/G.svg",
        "chordAudio": "/static/resources/G.mp3",
        "description": "Here is the G chord, your fingers should pressing the yellow dots on the strings.",
        "description2": "The following audio plays G chord. Listen several times and remember it!",
        "ukulele": "https://b7d3d5f9.rocketcdn.me/wp-content/themes/olympus/utimages/ukutabs-ukulele-full-vertical.png",
        "prev": "basic",
        "next": "2",
    },
    "2": {
        "id": 2,
        "chord": "F",
        "chordIMG": "https://b7d3d5f9.rocketcdn.me/chords/standard/F.svg",
        "chordAudio": "/static/resources/F.mp3",
        "description": "Here is the F chord, your fingers should pressing the yellow dots on the strings.",
        "description2": "The following audio plays F chord. Listen several times and remember it!",
        "ukulele": "https://b7d3d5f9.rocketcdn.me/wp-content/themes/olympus/utimages/ukutabs-ukulele-full-vertical.png",
        "prev": "1",
        "next": "3",
    },
    "3": {
        "id": 3,
        "chord": "C",
        "chordIMG": "https://b7d3d5f9.rocketcdn.me/chords/standard/C.svg",
        "chordAudio": "/static/resources/C.mp3",
        "description": "Here is the C chord, your fingers should pressing the yellow dots on the strings.",
        "description2": "The following audio plays C chord. Listen several times and remember it!",
        "ukulele": "https://b7d3d5f9.rocketcdn.me/wp-content/themes/olympus/utimages/ukutabs-ukulele-full-vertical.png",
        "prev": "2",
        "next": "quiz",
   },
}

# ROUTES
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/learn/basic')
def basic():
    return render_template('basic.html')

@app.route('/learn/basic-contd')
def basic_contd():
    return render_template('basic-contd.html')

@app.route('/learn/<id>')
def learn_fingering(id=None):
    global learnData
    data = learnData[id]

    return render_template('learn-fingering.html', data=data)

@app.route('/learn/<id>/sound')
def learn_sound(id=None):
    global learnData
    data = learnData[id]

    return render_template('learn-sound.html', data=data)

if __name__ == '__main__':
   app.run(debug = True)