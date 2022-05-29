import sqlite3
import os
from flask import g

DATABASE = 'persons.db'
path_sql = os.path.join("resources", "db.sql")

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    
    return db

def init_db(app):
    with app.app_context():
        db = get_db()
        with app.open_resource(path_sql, mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()