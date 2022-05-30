from services.db import get_db

def run(query):
    
    db = get_db()
    cursor = db.cursor()
    try:
        cursor.execute(query)
        db.commit()
    except:
        raise Exception("Failed query delete")
    finally:
        db.close()