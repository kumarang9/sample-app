from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():

    db_host = os.getenv("DB_HOST", "Not Configured")
    db_user = os.getenv("DB_USER", "Not Configured")

    return f"""
    <h1>Application Running Successfully</h1>

    <h2>AWS EKS Demo Application</h2>

    <p><b>Database Host:</b> {db_host}</p>

    <p><b>Database User:</b> {db_user}</p>

    <p><b>Environment:</b> Production</p>
    """

@app.route("/health")
def health():
    return {
        "status": "UP"
    }

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000
    )
