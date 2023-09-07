from flask import Flask
from flask_cors import CORS
from controller.test_controller import test_contoller
from controller.auth_controller import auth_controller


app = Flask(__name__)


CORS(app, supports_credentials=True)


app.register_blueprint(test_contoller, url_prefix="/api/v1/test")
app.register_blueprint(auth_controller, url_prefix="/api/v1/auth")

if __name__ == "__main__":
    app.run(port=5000)