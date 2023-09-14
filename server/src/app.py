from flask import Flask
from flask_cors import CORS
from controller.auth_controller import auth_controller
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()

CORS(app, supports_credentials=True, origins=["http://localhost:3000"])

app.register_blueprint(auth_controller, url_prefix="/api/v1/auth")

if __name__ == "__main__":
    app.run(port=5000)
