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
        "prev": "1",
        "next": "3",
        "ukulele": "https://b7d3d5f9.rocketcdn.me/wp-content/themes/olympus/utimages/ukutabs-ukulele-full-vertical.png",
        "fingerings": {
            "1": "5",
            "2": "14",
         }
    },
    "3": {
        "id": 3,
        "chord": "C",
        "chordIMG": "https://b7d3d5f9.rocketcdn.me/chords/standard/C.svg",
        "chordAudio": "/static/resources/C.mp3",
        "prev": "2",
        "next": "4",
        "ukulele": "https://b7d3d5f9.rocketcdn.me/wp-content/themes/olympus/utimages/ukutabs-ukulele-full-vertical.png",
        "fingerings": {
            "3": "3"
        }
   },
       "4": {
        "id": 4,
        "chord": "A",
        "chordIMG": "https://b7d3d5f9.rocketcdn.me/chords/standard/A.svg",
        "chordAudio": "/static/resources/A.mp3",
        "prev": "3",
        "next": "5",
        "ukulele": "https://b7d3d5f9.rocketcdn.me/wp-content/themes/olympus/utimages/ukutabs-ukulele-full-vertical.png",
        "fingerings": {
            "1": "9",
            "2": "14"
        }
   },
        "5": {
        "id": 5,
        "chord": "Am",
        "chordIMG": "https://b7d3d5f9.rocketcdn.me/chords/standard/Am.svg",
        "chordAudio": "/static/resources/Am.mp3",
        "prev": "4",
        "next": "",
        "ukulele": "https://b7d3d5f9.rocketcdn.me/wp-content/themes/olympus/utimages/ukutabs-ukulele-full-vertical.png",
        "fingerings": {
            "2": "14"
        }
   },

}

quiz_data = [ 
    {
        "id": "1", 
        "type": "0", 
        "image":["https://b7d3d5f9.rocketcdn.me/chords/standard/C.svg"], 
        "audio": ["/static/resources/A.mp3","/static/resources/C.mp3","/static/resources/G.mp3"],
        "target": "C",
        "next":"2",
        "ukulele": "https://b7d3d5f9.rocketcdn.me/wp-content/themes/olympus/utimages/ukutabs-ukulele-full-vertical.png",
        "correct": "B",
        "user": "",
        "learn_id":"3"
    },
    {
        "id": "2", 
        "type": "0", 
        "image":["https://b7d3d5f9.rocketcdn.me/chords/standard/G.svg"], 
        "audio": ["/static/resources/C.mp3","/static/resources/F.mp3","/static/resources/G.mp3"],
        "target": "G",
        "next":"3",
        "ukulele": "https://b7d3d5f9.rocketcdn.me/wp-content/themes/olympus/utimages/ukutabs-ukulele-full-vertical.png",
        "correct": "C",
        "user": "",
        "learn_id":"1"
    },
    {
        "id": "3", 
        "type": "0", 
        "image":["https://b7d3d5f9.rocketcdn.me/chords/standard/F.svg"], 
        "audio": ["/static/resources/F.mp3","/static/resources/A.mp3","/static/resources/G.mp3"],
        "target": "F",
        "next":"4",
        "ukulele": "https://b7d3d5f9.rocketcdn.me/wp-content/themes/olympus/utimages/ukutabs-ukulele-full-vertical.png",
        "correct": "A",
        "user": "",
        "learn_id":"2"
    },
    {
        "id": "4", 
        "type": "0", 
        "image":["https://b7d3d5f9.rocketcdn.me/chords/standard/A.svg"], 
        "audio": ["/static/resources/A.mp3","/static/resources/C.mp3","/static/resources/G.mp3"],
        "target": "A",
        "next":"5",
        "ukulele": "https://b7d3d5f9.rocketcdn.me/wp-content/themes/olympus/utimages/ukutabs-ukulele-full-vertical.png",
        "correct": "A",
        "user": "",
        "learn_id":"4"
    },
    {
        "id": "5", 
        "type": "0", 
        "image":["https://b7d3d5f9.rocketcdn.me/chords/standard/Am.svg"], 
        "audio": ["/static/resources/C.mp3","/static/resources/Am.mp3","/static/resources/F.mp3"],
        "target": "Am",
        "next":"6",
        "ukulele": "https://b7d3d5f9.rocketcdn.me/wp-content/themes/olympus/utimages/ukutabs-ukulele-full-vertical.png",
        "correct": "B",
        "user": "",
        "learn_id":"5"
    },
    {
        "id": "6", 
        "type": "1", 
        "image":["https://b7d3d5f9.rocketcdn.me/chords/standard/C.svg"], 
        "target": "C",
        "next":"7",
        "ukulele": "https://b7d3d5f9.rocketcdn.me/wp-content/themes/olympus/utimages/ukutabs-ukulele-full-vertical.png",
        "correct": {
            "1": "",
            "2": "",
            "3": "3",
            "4": ""
        },
        "user":"",
        "learn_id":"3"
    },
        {
        "id": "7", 
        "type": "1", 
        "image":["https://b7d3d5f9.rocketcdn.me/chords/standard/G.svg"], 
        "target": "G",
        "next":"8",
        "ukulele": "https://b7d3d5f9.rocketcdn.me/wp-content/themes/olympus/utimages/ukutabs-ukulele-full-vertical.png",
        "correct": {
            "1": "10",
            "2": "2",
            "3": "7",
            "4": ""
        },
        "user":"",
        "learn_id":"1"
    },
        {
        "id": "8", 
        "type": "1", 
        "image":["https://b7d3d5f9.rocketcdn.me/chords/standard/F.svg"], 
        "audio": ["/static/resources/C.mp3","/static/resources/F.mp3","/static/resources/G.mp3"],
        "target": "F",
        "next":"9",
        "ukulele": "https://b7d3d5f9.rocketcdn.me/wp-content/themes/olympus/utimages/ukutabs-ukulele-full-vertical.png",
        "correct": {
            "1": "5",
            "2": "14",
            "3": "",
            "4": ""
         },
        "user": "",
        "learn_id":"2"
    },
            {
        "id": "9", 
        "type": "1", 
        "image":["https://b7d3d5f9.rocketcdn.me/chords/standard/Am.svg"], 
        "target": "Am",
        "next":"10",
        "ukulele": "https://b7d3d5f9.rocketcdn.me/wp-content/themes/olympus/utimages/ukutabs-ukulele-full-vertical.png",
        "correct": {
            "1": "",
            "2": "14",
            "3": "",
            "4": ""
         },
        "user": "",
        "learn_id":"5"
    },
            {
        "id": "10", 
        "type": "1", 
        "image":["https://b7d3d5f9.rocketcdn.me/chords/standard/A.svg"], 
        "target": "A",
        "next":"",
        "ukulele": "https://b7d3d5f9.rocketcdn.me/wp-content/themes/olympus/utimages/ukutabs-ukulele-full-vertical.png",
        "correct": {
            "1": "9",
            "2": "14",
            "3": "",
            "4": ""
         },
        "user": "",
        "learn_id":"4"
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

@app.route('/learn/check')
def check_ready():
    return render_template('learning_quiz_check.html')

@app.route('/learn/<id>')
def learn_fingering(id=None):
    global learnData
    data = learnData[id]

    return render_template('learn-fingering.html', data=data)

@app.route('/quiz/<id>')
def quiz(id=None):
    id = int(id)
    selected_data = quiz_data[id-1]
    if selected_data["type"] == '0':
        return render_template('quiz.html', data=selected_data)
    elif selected_data["type"] == '1':
        return render_template('quiz_fingering.html', data = selected_data)

@app.route('/quiz/result')
def quiz_feedback():

    result,review_id,num = checkAnswer()

    review_links = [[i,learnData[i]["chord"]] for i in review_id]
    # result["correct_num"] = num
    print(review_links)
    data = {
        "result":result,
        "review":review_links,
        "correctNum": num
    }
    print(data)
    return render_template('quiz-result.html', data = data)

# AJAX Functions
@app.route('/quiz/save_user_response', methods=['POST'])
def save_user_response():
    global quiz_data

    json_data = request.get_json()
    i = (int(json_data["id"])) - 1 
    response = json_data["user"]
    
    quiz_data[i]["user"] = response   # NEED TO FIX I DOESNT WORK
    
    return jsonify(quiz_data=quiz_data)

def checkAnswer():
    result = {}
    # review = set()
    review_id = set()
    correct_num = 0
    for i in range(10):
        if quiz_data[i]["correct"] == quiz_data[i]['user']:
            result[i] = True
            correct_num += 1
        else:
            result[i] = False
            # review.add(quiz_data[i]['target'])
            review_id.add(quiz_data[i]["learn_id"])
    return result, review_id, correct_num


if __name__ == '__main__':
   app.run(debug = True)
