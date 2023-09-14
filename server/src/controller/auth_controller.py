from flask import Blueprint, jsonify, request
from service.auth_service import AuthService
from decorator.jwt_required import jwt_required
import jwt

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


@auth_controller.route("/verify", methods=["POST"])
@jwt_required
def verify_user():
    verify_token = request.cookies.get("access_token")
    if verify_token:
        decoded_token = jwt.decode(
            verify_token, "secret",
            algorithms=["HS256"]
        )
        token_information = decoded_token["payload"]
        user_information = {
            "id": token_information["id"],
            "email": token_information["email"]
        }
        return jsonify({"success": "true", "user_information": user_information}), 200