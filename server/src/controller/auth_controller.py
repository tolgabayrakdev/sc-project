from flask import Blueprint, jsonify, request
from database import get_cursor
from service.auth_service import AuthService

auth_controller = Blueprint("auth_controller", __name__)
cursor = get_cursor()


@auth_controller.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    email = data["email"]
    password = data["password"]
    result = AuthService.login(email, password)
    return result, 200


@auth_controller.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    result = AuthService.register(user=data)
    return result, 201
    
