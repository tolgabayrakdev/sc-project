from flask import Blueprint, jsonify
from database import get_cursor


test_contoller = Blueprint("test_contoller", __name__)
cursor = get_cursor()  # Veritabanı bağlantısını al


@test_contoller.route("/deneme", methods=["GET"])
def test():
    try:
        text = "SELECT * FROM users"
        cursor.execute(text)

        # Sonuçları al
        sonuclar = cursor.fetchall()
        
        return jsonify({"result": sonuclar})
    except Exception as e:
        return jsonify({"error": str(e)})
