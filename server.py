from flask import Flask
from flask import render_template
from flask import Response, request, jsonify, json
from itsdangerous import json
app = Flask(__name__)



learnData = {
    "1": {
        "id": 1,
        "chord": "G",
        "chordIMG": "https://b7d3d5f9.rocketcdn.me/chords/standard/G.svg",
        "chordAudio": "/static/resources/G.mp3",
        "description": "Here is the G chord, your fingers should pressing the yellow dots on the strings.",
        "description2": "Here is the sound for the G chord!!!",
        "prev": "",
        "next": "2",
        "ukulele": "https://b7d3d5f9.rocketcdn.me/wp-content/themes/olympus/utimages/ukutabs-ukulele-full-vertical.png",
        "fingerings": {
            "1": "10",
            "2": "2",
            "3": "7",
        }
    },
    "2": {
        "id": 2,
        "chord": "F",
        "chordIMG": "https://b7d3d5f9.rocketcdn.me/chords/standard/F.svg",
        "chordAudio": "/static/resources/F.mp3",
        "description": "Here is the F chord, your fingers should pressing the yellow dots on the strings.",
        "description2": "Here is the sound for the F chord!!!",
        "prev": "1",
        "next": "3",
        "ukulele": "https://b7d3d5f9.rocketcdn.me/wp-content/themes/olympus/utimages/ukutabs-ukulele-full-vertical.png",
        "fingerings": {
            "1": "5",
            "2": "10",
         }
    },
    "3": {
        "id": 3,
        "chord": "C",
        "chordIMG": "https://b7d3d5f9.rocketcdn.me/chords/standard/C.svg",
        "chordAudio": "/static/resources/G.mp3",
        "description": "Here is the C chord, your fingers should pressing the yellow dots on the strings.",
        "description2": "Here is the sound for the C chord!!!",
        "prev": "2",
        "next": "",
        "ukulele": "https://b7d3d5f9.rocketcdn.me/wp-content/themes/olympus/utimages/ukutabs-ukulele-full-vertical.png",
        "fingerings": {
            "3": "3"
        }
   }
}

quiz_data = [ 
    {
        "id": "1", 
        "type": "0", 
        "image":["https://b7d3d5f9.rocketcdn.me/chords/standard/C.svg"], 
        "audio": ["/static/resources/C.mp3","/static/resources/F.mp3","/static/resources/G.mp3"],
        "target": "C",
        "next":"2",
        "previous":"",
        "ukulele": "https://b7d3d5f9.rocketcdn.me/wp-content/themes/olympus/utimages/ukutabs-ukulele-full-vertical.png"
    },
    {
        "id": "2", 
        "type": "0", 
        "image":["https://b7d3d5f9.rocketcdn.me/chords/standard/G.svg"], 
        "audio": ["/static/resources/C.mp3","/static/resources/F.mp3","/static/resources/G.mp3"],
        "target": "G",
        "next":"3",
        "previous":"1",
        "ukulele": "https://b7d3d5f9.rocketcdn.me/wp-content/themes/olympus/utimages/ukutabs-ukulele-full-vertical.png"
    },
    {
        "id": "3", 
        "type": "0", 
        "image":["https://b7d3d5f9.rocketcdn.me/chords/standard/F.svg"], 
        "audio": ["/static/resources/C.mp3","/static/resources/F.mp3","/static/resources/G.mp3"],
        "target": "F",
        "next":"4",
        "previous":"2",
        "ukulele": "https://b7d3d5f9.rocketcdn.me/wp-content/themes/olympus/utimages/ukutabs-ukulele-full-vertical.png"
    },
        {
        "id": "4", 
        "type": "1", 
        "image":["https://b7d3d5f9.rocketcdn.me/chords/standard/C.svg"], 
        "audio": ["/static/resources/C.mp3","/static/resources/F.mp3","/static/resources/G.mp3"],
        "target": "C",
        "next":"5",
        "previous":"",
        "ukulele": "https://b7d3d5f9.rocketcdn.me/wp-content/themes/olympus/utimages/ukutabs-ukulele-full-vertical.png",

    },
        {
        "id": "5", 
        "type": "1", 
        "image":["https://b7d3d5f9.rocketcdn.me/chords/standard/G.svg"], 
        "audio": ["/static/resources/C.mp3","/static/resources/F.mp3","/static/resources/G.mp3"],
        "target": "G",
        "next":"6",
        "previous":"1",
        "ukulele": "https://b7d3d5f9.rocketcdn.me/wp-content/themes/olympus/utimages/ukutabs-ukulele-full-vertical.png"
    },
        {
        "id": "6", 
        "type": "1", 
        "image":["https://b7d3d5f9.rocketcdn.me/chords/standard/F.svg"], 
        "audio": ["/static/resources/C.mp3","/static/resources/F.mp3","/static/resources/G.mp3"],
        "target": "F",
        "next":"",
        "previous":"2",
        "ukulele": "https://b7d3d5f9.rocketcdn.me/wp-content/themes/olympus/utimages/ukutabs-ukulele-full-vertical.png"
    }
]

quiz_results = [
    {
        "id": "1",
        "correct": "0",
        "user": ""
    },
    {
        "id": "2",
        "correct": "2",
        "user": ""
    },
        {
        "id": "3",
        "correct": "1",
        "user": ""
    },
    {
        "id": "4",
        "correct": {
            "1": "",
            "2": "",
            "3": "3",
            "4": ""
        },
        "user":""
    },
    {
        "id": "5",
        "correct": {
            "1": "10",
            "2": "2",
            "3": "7",
            "4": ""
        },
        "user":""
    },
    {
        "id": "6",
        "correct": {
            "1": "5",
            "2": "10",
            "3": "",
            "4": ""
         },
        "user": ""
    }
]

# ROUTES
@app.route('/')
def home():
    return render_template('start.html')

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

@app.route('/quiz/<id>')
def quiz(id=None):
    id = int(id)
    selected_data = quiz_data[id-1]
    if selected_data["type"] == '0':
        return render_template('quiz.html', data=selected_data)
    elif selected_data["type"] == '1':
        print("here")
        return render_template('quiz_fingering.html', data = selected_data)

@app.route('/quiz/result')
def quiz_feedback():
    return render_template('quiz-result.html', data=quiz_results)

# AJAX Functions
@app.route('/quiz/save_user_response', methods=['POST'])
def save_user_response():
    global quiz_results

    json_data = request.get_json()
    i = (int(json_data["id"])) - 1 
    response = json_data["user"]

    quiz_results[i]["user"] = response   # NEED TO FIX I DOESNT WORK

    return jsonify(quiz_results=quiz_results)

    #how do we change this so that it works for the fingering?
if __name__ == '__main__':
   app.run(debug = True)
