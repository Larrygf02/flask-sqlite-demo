from flask import Blueprint, jsonify, request
from services.db import get_db
from services.db.models import PersonManager

router = Blueprint('v1', __name__, url_prefix='/v1')

@router.route('/person/<person_id>', methods=['GET'])
def get_person(person_id):
    manager = PersonManager()
    result = manager.get_one_person(person_id)
    return jsonify({"result": result})

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

@router.route('/person/<person_id>', methods=["DELETE"])
def delete_person(person_id):
    manager = PersonManager()
    manager.delete_person(person_id)
    return jsonify({"success": True})
