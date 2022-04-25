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
        "description2": "Here is the sound for the G chord!!!",
        "prev": "basic",
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
        "next": "quiz",
        "ukulele": "https://b7d3d5f9.rocketcdn.me/wp-content/themes/olympus/utimages/ukutabs-ukulele-full-vertical.png",
        "fingerings": {
            "2": ""
        }
   }
}




# ROUTES
quiz_data = [ 
    {
        "id": "1", 
        "type": "0", 
        "image":["https://b7d3d5f9.rocketcdn.me/chords/standard/C.svg"], 
        "audio": ["/static/resources/C.mp3","/static/resources/F.mp3","/static/resources/G.mp3"],
        "target": "C",
        "next":"2",
        "previous":"",
        "ukulele": "https://b7d3d5f9.rocketcdn.me/wp-content/themes/olympus/utimages/ukutabs-ukulele-full-vertical.png",
        "fingerings": {
            "finger1": "",
            "finger2": "",
            "finger3": "3",
            "finger4": ""
        }

    },
    {
        "id": "2", 
        "type": "0", 
        "image":["https://b7d3d5f9.rocketcdn.me/chords/standard/G.svg"], 
        "audio": ["/static/resources/C.mp3","/static/resources/F.mp3","/static/resources/G.mp3"],
        "target": "G",
        "next":"3",
        "previous":"1",
        "ukulele": "https://b7d3d5f9.rocketcdn.me/wp-content/themes/olympus/utimages/ukutabs-ukulele-full-vertical.png",
         "fingerings": {
            "finger1": "10",
            "finger2": "2",
            "finger3": "7",
            "finger4": ""
        }

    },
    {
        "id": "3", 
        "type": "0", 
        "image":["https://b7d3d5f9.rocketcdn.me/chords/standard/F.svg"], 
        "audio": ["/static/resources/C.mp3","/static/resources/F.mp3","/static/resources/G.mp3"],
        "target": "F",
        "next":"4",
        "previous":"2",
        "ukulele": "https://b7d3d5f9.rocketcdn.me/wp-content/themes/olympus/utimages/ukutabs-ukulele-full-vertical.png",
         "fingerings": {
            "finger1": "5",
            "finger2": "10",
            "finger3": "",
            "finger4": ""
         }

    }
]
quiz_result = []

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


@app.route('/quiz/<id>')
def quiz(id=None):
    id = int(id)
    selected_data = quiz_data[id-1]
    return render_template('quiz.html', data=selected_data) 

@app.route('/quiz/<id>/fingering')
def quiz_fingering(id=None):
    id = int(id)
    finger_data = quiz_data[id-1]
    return render_template('quiz_fingering.html', data = finger_data)

@app.route('/quiz/result')
def quiz_feedback():
    return render_template('quiz-result.html', data=quiz_result)

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