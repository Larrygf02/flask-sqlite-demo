import json
from flask import Blueprint, jsonify, request
from services.db import get_db

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
    print(body)
    first_name = body['first_name']
    last_name = body['last_name']
    email = body['email']
    dni = body['dni']
    data = [first_name, last_name, email, dni]
    db = get_db()
    cursor = db.cursor()
    cursor.execute("INSERT INTO person (first_name, last_name, email, dni) values(?, ?, ?, ?)", data)
    db.commit()
    db.close()
    return jsonify({"success": True})

@router.route('/persons', methods=['GET'])
def get_persons():
    db = get_db()
    cursor = db.cursor()
    result = cursor.execute("select * from person").fetchall()
    columns = [description[0] for description in cursor.description]
    persons = []
    for item in result:
        person = dict()
        for key, value in zip(columns, list(item)):
            person[key] = value
        persons.append(person)
    db.close()
    return jsonify({"result": persons})
