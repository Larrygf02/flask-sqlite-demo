from flask import Flask
from .routes import configure_routes
from services.db import init_db

def initalize_server():
    app = Flask(__name__)
    configure_routes(app)
    init_db(app)
    return app