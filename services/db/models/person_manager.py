from utils import valid_payload, get_fields
from services.db.query import insert, select

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