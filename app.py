from flask import Flask, render_template, session
from flask_session import Session
import os

app = Flask(__name__)

# Configure session to use filesystem (to persist count across users)
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route('/')
def home():
    # Initialize the counter
    if 'counter' not in session:
        session['counter'] = 0

    # Increment the counter
    session['counter'] += 1

    # Display the count
    return f"<h1>Welcome to the Website!</h1><p>You are visitor number: {session['counter']}</p>"

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
