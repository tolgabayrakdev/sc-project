from flask import request, jsonify
from functools import wraps
import jwt
import os
from util.helper import Helper

def jwt_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            auth_header = request.cookies.get('access_token')
            if auth_header:
                return func(*args, **kwargs)
            else:
                return jsonify({"message": "Missing access token"}), 403
        except jwt.exceptions.InvalidSignatureError:
            return jsonify({"message": "Invalid access token"}), 401
        except jwt.exceptions.ExpiredSignatureError:
            return jsonify({"message": "Access token has expired"}), 401
        except jwt.exceptions.DecodeError:
            return jsonify({"message": "Invalid access token"}), 401

    return wrapper