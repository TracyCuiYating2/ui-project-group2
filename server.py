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

@app.route('/learn/quiz')
def quiz():
    return render_template('quiz.html')

if __name__ == '__main__':
   app.run(debug = True)