from flask import Blueprint, jsonify, request
from database import get_cursor
from service.auth_service import AuthService


test_contoller = Blueprint("test_contoller", __name__)
cursor = get_cursor()  # Veritabanı bağlantısını al


@test_contoller.route("/deneme", methods=["POST"])
def test():
        data = request.get_json()
        email = data["email"]
        text = "SELECT * FROM users"
        cursor.execute(text)
        
        # Sonuçları al
        sonuclar = cursor.fetchall()
        
        return jsonify({"result": sonuclar})

