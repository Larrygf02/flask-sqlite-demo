from utils import valid_payload, get_fields, valid_update, get_query_update
from services.db.query import insert, select, delete, update

class PersonManager():
    def __init__(self):
        self.PERSON_COLUMNS = ['first_name', 'last_name', 'email', 'dni']

    def create_person(self, payload):
        if valid_payload(payload, self.PERSON_COLUMNS):
            data = get_fields(payload, self.PERSON_COLUMNS)
            query = "INSERT INTO person (first_name, last_name, email, dni) values(?, ?, ?, ?)"
            insert(query, data)

    def get_persons(self):
        query = "SELECT * from person"
        result = select(query)
        return result

    def get_one_person(self, person_id):
        query = f"SELECT * from person where person_id = {person_id}"
        result = select(query)
        return result[0]

    def delete_person(self, person_id):
        query = f"Delete from person where person_id = {person_id}"
        delete(query)

    def update_person(self, payload, person_id):
        if valid_update(payload, self.PERSON_COLUMNS):
            query, data = get_query_update(payload, {'column': 'person_id', 'value': person_id}, 'person')
            update(query, data)