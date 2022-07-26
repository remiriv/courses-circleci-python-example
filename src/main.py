from flask import Flask
from src.app import app

flask_engine = Flask(__name__)
flask_engine.register_blueprint(app)

if __name__ == "server":
    flask_engine.run(host="0.0.0.0", port=5000)
