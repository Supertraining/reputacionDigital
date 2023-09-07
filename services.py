import sqlite3
from models import Author
def create_author(new_author: Author, my_target_field: str):

    conn = sqlite3.connect("./db/main.db")
    cursor = conn.cursor()

    setattr(new_author, my_target_field, 
            getattr(new_author, my_target_field).upper())
    
    author = new_author.save()

    conn.commit()
    cursor.close()
    conn.close()

    return author

def get_author_id(id):
    
    conn = sqlite3.connect("./db/main.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM authors WHERE id = ?", (id,))
    result = cursor.fetchone()

    columns = [column[0] for column in cursor.description]
    author = dict(zip(columns, result))

    cursor.close()
    conn.close()

    return author