from pydoc import describe
from services.db import get_db

def run(query):
    
    db = get_db()
    cursor = db.cursor()
    try:
        result = cursor.execute(query).fetchall()
        columns = [description[0] for description in cursor.description]
        data = _transform(result, columns)
        return data
    except:
        raise Exception("Failed query select")
    finally:
        db.close()

def _transform(result, columns):
    data = []
    for item in result:
        d = dict()
        for key, value in zip(columns, list(item)):
            d[key] = value
        data.append(d)
    return data
        
        
    