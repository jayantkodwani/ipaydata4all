from flask import Flask, render_template
import sqlite3
import os

app = Flask(__name__)

# Database file
DB_FILE = "counter.db"

# Initialize the database
def init_db():
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS visitor_count (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                count INTEGER NOT NULL
            )
        """)
        # Insert initial count if table is empty
        cursor.execute("SELECT COUNT(*) FROM visitor_count")
        if cursor.fetchone()[0] == 0:
            cursor.execute("INSERT INTO visitor_count (count) VALUES (0)")
        conn.commit()

@app.route('/')
def home():
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        # Fetch the current count
        cursor.execute("SELECT count FROM visitor_count WHERE id = 1")
        current_count = cursor.fetchone()[0]
        
        # Increment the counter
        new_count = current_count + 1
        cursor.execute("UPDATE visitor_count SET count = ? WHERE id = 1", (new_count,))
        conn.commit()

    return f"<h1>Welcome to the Website!</h1><p>You are visitor number: {new_count}</p>"

if __name__ == '__main__':
    # Initialize the database
    init_db()

    # Run the app
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
