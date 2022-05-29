from flask import Flask
from .routes import configure_routes

def initalize_server():
    app = Flask(__name__)
    configure_routes(app)
    return app