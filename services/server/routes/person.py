import json
from flask import Blueprint, jsonify
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
    db = get_db()
    cursor = db.cursor()
    cursor.execute("INSERT INTO person (first_name, last_name, email, dni) values('raul', 'larriega', 'raulgf_02@hotmail.com', '7293828')")
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
