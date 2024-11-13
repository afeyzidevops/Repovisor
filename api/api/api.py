from flask import Flask
from waitress import serve

def create_app():
    app = Flask(__name__)
    return app