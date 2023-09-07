from flask import Flask
from flask_cors import CORS
from controller.test_controller import test_contoller


app = Flask(__name__)


CORS(app, supports_credentials=True)


app.register_blueprint(test_contoller, url_prefix="/api/v1/test")

if __name__ == "__main__":
    app.run(port=5000)