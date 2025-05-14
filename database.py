import sqlite3

def init_db():
    conn = sqlite3.connect("interns.db")
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS interns (
            unique_code TEXT PRIMARY KEY,
            name TEXT,
            email TEXT,
            date TEXT,
            status TEXT
        )
    """)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    print("Database initialized.")