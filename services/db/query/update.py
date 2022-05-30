from services.db import get_db

def run(query, data):
    
    db = get_db()
    cursor = db.cursor()
    try:
        cursor.execute(query, data)
        db.commit()
    except:
        raise Exception("Failed query update")
    finally:
        db.close()