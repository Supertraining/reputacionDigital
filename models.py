import sqlite3
from pydantic import BaseModel
import uuid

class Author(BaseModel):
    field_1: str
    author: str
    description: str
    my_numeric_field: int

    def save(self):
        conn = sqlite3.connect("./db/main.db")
        try:
            id = uuid.uuid4().hex   
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO authors (id, field_1, author, description, my_numeric_field)
                VALUES (?, ?, ?, ?, ?)
                """,
                (id, self.field_1, self.author, self.description, self.my_numeric_field),
            )

            conn.commit()

            cursor.execute("SELECT * FROM authors WHERE id = ?", (id,))
            result = cursor.fetchone()
            columns = [column[0] for column in cursor.description]
            author = dict(zip(columns, result))
            return author
            
        finally:
            conn.close()