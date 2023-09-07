from util.helper import Helper
from database import get_cursor
from werkzeug.exceptions import NotFound, InternalServerError

cursor = get_cursor()

class AuthService:

    @staticmethod
    def login(email: str, password: str):
        try:
            text = "SELECT * FROM users WHERE email = %s and password = %s"
            cursor.execute(text, (email,password,))
            result = cursor.fetchall()
            if result:
                return result
            else:
                raise NotFound(description="User not found! Check your credential")
        except InternalServerError as e:
            raise InternalServerError(description="Database Error!")

        
        
    @staticmethod
    def register(user: dict):
        hash_password = Helper.generate_hash_password(password=user["password"])
        try:
            cursor.execute("BEGIN")
            text = """
                    INSERT INTO users(username, email, password, created_at, updated_at)
                    VALUES(%s, %s, %s, now(), now())
                """
            cursor.execute(text, (user["username"], user["email"], hash_password))
            cursor.connection.commit()
            message = {"message": "User created successful."}
            return message
        except InternalServerError as e:
            cursor.execute("ROLLBACK")
            raise InternalServerError(description="Database Error!")

        