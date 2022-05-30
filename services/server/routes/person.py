import json
from flask import Blueprint, jsonify, request
from services.db import get_db
from services.db.models import PersonManager

router = Blueprint('v1', __name__, url_prefix='/v1')

@router.route('/person', methods=['GET'])
def get_person():
    data = {
        "person": "juan"
    }
    return jsonify(data)

@router.route('/person', methods=['POST'])
def create_person():
    body = request.get_json()
    manager = PersonManager()
    manager.create_person(body)
    return jsonify({"success": True})

@router.route('/persons', methods=['GET'])
def get_persons():
    manager = PersonManager()
    persons = manager.get_persons()
    return jsonify({"result": persons})
