from flask import Flask, render_template, url_for, request
from datetime import datetime
from flask_cors import CORS

import json



app = Flask(__name__)

app.config.from_object(__name__)

CORS(app, resources={r"/api/*": {"origins": "*"}})
CORS(app, resources={r"/*": {"origins": "http://localhost:5173","allow_headers":"Access-Allow-Origin"}})


# Routes 
@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def msg():
    return 'This is the homepage of the application JE.'

@app.route('/library', methods = ['GET'])
def all_scientists():
	return 'All scientists list from backend'



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
