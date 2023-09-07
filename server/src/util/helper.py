import time
import hashlib
import jwt


class Helper:
    @staticmethod
    def generate_hash_password(password: str):
        salt = "SaltSecretKey"
        return (
            hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ":" + salt
        )

    @staticmethod
    def match_hashed_text(hashed_text, provided_text):
        _hashed_text, salt = hashed_text.split(":")
        return (
            _hashed_text
            == hashlib.sha256(salt.encode() + provided_text.encode()).hexdigest()
        )

    @staticmethod
    def generate_access_token(payload):
        return jwt.encode(
            {"payload": payload, "exp": int(time.time() + 3000)},
            "secret",
            algorithm="HS256",
        )

    @staticmethod
    def generate_refresh_token(payload):
        return jwt.encode({"payload": payload}, "secret", algorithm="HS256")