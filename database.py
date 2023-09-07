import sqlite3

def create_tables():
  conn = sqlite3.connect("./db/main.db")
  try:
    cursor = conn.cursor()
    cursor.execute("""
      CREATE TABLE IF NOT EXISTS authors (
        id VARCHAR(36) PRIMARY KEY,
        field_1 TEXT,
        author TEXT,
        description TEXT,
        my_numeric_field INTEGER
      )
      """)
  
    conn.commit()
  finally:
    conn.close