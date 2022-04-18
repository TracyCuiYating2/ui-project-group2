from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
from itsdangerous import json
app = Flask(__name__)

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
    return render_template('learn-fingering.html')

@app.route('/learn/2')
def learn_sound():
    return render_template('learn-sound.html')

if __name__ == '__main__':
   app.run(debug = True)