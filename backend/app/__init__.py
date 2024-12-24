from flask import Flask
from flask_restx import Api
from app.routes.scientist_crud import scientist_api

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')  # Cargar configuraciones desde config.py
    api = Api(app, title="Scientist API", version="1.0", description="API for managing scientists")

    # Registrar namespaces
    api.add_namespace(scientist_api, path='/scientists')

    return app

