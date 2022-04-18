from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
from itsdangerous import json
app = Flask(__name__)

learnData = [
    {
        "id": 1,
        "chord": "C",
        "chordIMG": "https://b7d3d5f9.rocketcdn.me/chords/standard/C.svg",
        "chordAudio": "../rescourse/C.mp3"
    },
    {
        "id": 2,
        "chord": "F",
        "chordIMG": "https://b7d3d5f9.rocketcdn.me/chords/standard/F.svg",
        "chordAudio": "../rescourse/F.mp3"
    },
    {
        "id": 3,
        "chord": "G",
        "chordIMG": "https://b7d3d5f9.rocketcdn.me/chords/standard/G.svg",
        "chordAudio": "../rescourse/C.mp3"
    }
]



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

@app.route('/learn/1')
def learn_fingering():
    return render_template('learn-fingering.html', learnData = learnData)

@app.route('/learn/2')
def learn_sound():
    return render_template('learn-sound.html')

if __name__ == '__main__':
   app.run(debug = True)