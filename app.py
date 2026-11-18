
from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>Automated CI/CD Pipeline</title>
    </head>
    <body>
        <h1>Automated CI/CD Pipeline</h1>
        <h2>Version 2 - Automatic Deployment Successful!</h2>
        <p>Welcome to my containerized web application.</p>
    </body>
    </html>
    """

@app.route("/health")
def health():
    return {"status": "healthy"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
