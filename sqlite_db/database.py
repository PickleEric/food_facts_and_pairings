import sqlite3
from .config import db 

def create_table():
    try:
        with sqlite3.connect(db) as conn:
            conn.execute ('CREATE TABLE IF NOT EXISTS bookmark_db (food_search text, food text, beer text, cocktail text')

    except Exception as e:
        print('Error, please check connection', e)
    conn.close

def save_pairing(info):
    try:
        with sqlite3.connect(db)as conn:
            conn.execute(f'INSERT INTO bookmark_db VALUES(?, ?, ?, ?)'(info.food_search, info.food, info.beer, info.cocktail))
        return True
    except sqlite3.IntegrityError as e:
        raise NameError(f'Error already an entry') from e
    finally:
        conn.close()
            
def get_pairing_info():
    conn = sqlite3.connect(db)
    result = conn.execute('SELECT * FROM bookmark_db')
    print('Saved pairing:')
    for row in result:
        print(row)
    conn.close()