from flask import Flask, render_template, url_for, request
from datetime import datetime
from flask_cors import CORS

from app.config import Config ##proof 3
from app.models import Scientist
from app.services import ScientistService
from app.models.scientist_model import db


import json



app = Flask(__name__)

db.init_app(app)

app.config.from_object(__name__)

CORS(app, resources={r"/api/*": {"origins": "*"}})
CORS(app, resources={r"/*": {"origins": "http://localhost:5173","allow_headers":"Access-Allow-Origin"}})


# Routes 
@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def msg():
    return 'This is the homepage of the application JE.'

@app.route('/libraries', methods = ['GET'])
def all_scientists():
	return 'All scientists list from backend'


@app.route('/scientists', methods=['GET'])
def list_scientists():
    """Endpoint to list all scientists"""
    scientists = ScientistService.get_all_scientists()
    return jsonify([
        {
            "id": scientist.id,
            "name": scientist.name,
            "birthday": scientist.birthday.isoformat() if scientist.birthday else None,
            "description": scientist.description,
            "area": scientist.area,
        } for scientist in scientists
    ]), 200



if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Create the database tables if they don't exist
    app.run(debug=True)
