from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
from itsdangerous import json
app = Flask(__name__)



learnData ={
    "0": {
        "id": 0,
        "title": "G Chord",
        "img": "https://b7d3d5f9.rocketcdn.me/wp-content/themes/olympus/utimages/ukuchords/ukuchords_howtoreadchordcharts.png",
        "altText": "There's a single ukulele with some diagrams for where to place the fingers.",
        "prev": "basic",
        "next": "1",
        "audio": "/static/resources/G.mp3",
    },
    "1": {
        "id": 1,
        "title": "F Chord",
        "img": "https://b7d3d5f9.rocketcdn.me/wp-content/themes/olympus/utimages/ukuchords/ukuchords_howtoreadchordcharts.png",
        "altText": "There's a single ukulele with some diagrams for where to place the fingers.",
        "prev": "0",
        "next": "2",
        "audio": "/static/resources/F.mp3",
    },
    "2": {
        "id": 2,
        "title": "C Chord",
        "img": "https://b7d3d5f9.rocketcdn.me/wp-content/themes/olympus/utimages/ukuchords/ukuchords_howtoreadchordcharts.png",
        "altText": "There's a single ukulele with some diagrams for where to place the fingers.",
        "prev": "1",
        "next": "quiz",
        "audio": "/static/resources/C.mp3",
    },
}




# ROUTES
quiz_data = [ 
    {
        "id": "1", 
        "type": "0", 
        "image":["https://b7d3d5f9.rocketcdn.me/chords/standard/C.svg"], 
        "audio": ["/rescourse/C.mp3","/rescourse/F.mp3","/rescourse/G.mp3"],
        "target": "C",
        "next":"2",
        "previous":""
    },
    {
        "id": "2", 
        "type": "0", 
        "image":["https://b7d3d5f9.rocketcdn.me/chords/standard/G.svg"], 
        "audio": ["/rescourse/C.mp3","/rescourse/F.mp3","/rescourse/G.mp3"],
        "target": "G",
        "next":"3",
        "previous":"1"
    },
    {
        "id": "3", 
        "type": "0", 
        "image":["https://b7d3d5f9.rocketcdn.me/chords/standard/F.svg"], 
        "audio": ["/rescourse/C.mp3","/rescourse/F.mp3","/rescourse/G.mp3"],
        "target": "F",
        "next":"4",
        "previous":"2"
    }
]
quiz_result = []

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/learn/<id>')
def learn(id=None):
    global learnData
    data = learnData[id]

    return render_template('learn.html', data=data)


@app.route('/learn/basic')
def basic():
    return render_template('basic.html')

@app.route('/learn/basic-contd')
def basic_contd():
    return render_template('basic-contd.html')

@app.route('/learn/1')
def learn_fingering():
    return render_template('learn-fingering.html')

@app.route('/learn/2')
def learn_sound():
    return render_template('learn-sound.html')


@app.route('/quiz/<id>')
def quiz(id=None):
    id = int(id)
    selected_data = quiz_data[id-1]
    return render_template('quiz.html', data=selected_data) 

@app.route('/quiz/result')
def quiz_feedback():
    return render_template('quiz-result.html', data=quiz_result)

if __name__ == '__main__':
   app.run(debug = True)