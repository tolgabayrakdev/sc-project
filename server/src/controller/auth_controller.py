from flask import Blueprint, jsonify, request
from service.auth_service import AuthService
from decorator.jwt_required import jwt_required

auth_controller = Blueprint("auth_controller", __name__)


@auth_controller.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    email = data["email"]
    password = data["password"]
    result = AuthService.login(email, password)
    if result:
        response = jsonify({
            "access_token": result["access_token"],
            "refresh_token": result["refresh_token"]
        })
        response.set_cookie("access_token", result["access_token"], httponly=True)
        response.set_cookie("refresh_token", result["refresh_token"], httponly=True)
        return response, 200
    else:
        return jsonify({"message": "Error"}), 401

@auth_controller.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    result = AuthService.register(user=data)
    return result, 201
    


@auth_controller.route("/logout", methods=["POST"])
def logout():
    try:
        response = jsonify({"message": "Log out successfull."})
        response.delete_cookie("access_token")
        response.delete_cookie("refresh_token")
        return response, 200
    except:
        print("Error!")


@auth_controller.route("/secret", methods=["GET"])
@jwt_required
def secret_function():
    return jsonify({"message": "Hello from secret api!!!"}), 200