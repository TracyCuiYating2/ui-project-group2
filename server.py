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

if __name__ == '__main__':
   app.run(debug = True)