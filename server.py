from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
from itsdangerous import json
app = Flask(__name__)



learnData =[
    {
        "id": 0,
        "img": "https://b7d3d5f9.rocketcdn.me/wp-content/themes/olympus/utimages/ukuchords/ukuchords_howtoreadchordcharts.png",
        "altText": "There's a single ukulele with some diagrams for where to place the fingers."
    }
]




# ROUTES

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/learn')
def learn():
    #learnDataID = learnData[id]
    return render_template('learn.html', learnData = learnData)


@app.route('/learn/basic')
def basic():
    return render_template('basic.html')

@app.route('/learn/quiz')
def quiz():
    return render_template('quiz.html')

if __name__ == '__main__':
   app.run(debug = True)