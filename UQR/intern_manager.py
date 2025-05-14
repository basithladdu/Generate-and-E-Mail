import uuid
import sqlite3

def generate_unique_code():
    # Short version of a UUID; you may lengthen it if needed.
    return str(uuid.uuid4())[:8]

def save_intern_details(unique_code, name, email, date, status="verified"):
    conn = sqlite3.connect("interns.db")
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO interns (unique_code, name, email, date, status)
        VALUES (?, ?, ?, ?, ?)
    """, (unique_code, name, email, date, status))
    conn.commit()
    conn.close()

# Example usage:
if __name__ == "__main__":
    code = generate_unique_code()
    save_intern_details(code, "John Doe", "john.doe@example.com", "06 April 2025")
    print(f"Details for {code} saved.")