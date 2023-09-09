from util.helper import Helper
from database import get_db_connection
from werkzeug.exceptions import NotFound, InternalServerError
import psycopg2



class AuthService:
    @staticmethod
    def login(email: str, password: str):
        try:
            connection = get_db_connection()
            cursor = connection.cursor()
            text = "SELECT * FROM users WHERE email = %s and password = %s"
            cursor.execute(
                text,
                (
                    email,
                    password,
                ),
            )
            result = cursor.fetchall()
            connection.close()
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
            connection = get_db_connection()
            cursor = connection.cursor()
            
            cursor.execute("BEGIN")
            text = """
              INSERT INTO users(username, email, password, created_at, updated_at)
                    VALUES(%s, %s, %s, now(), now())
                """
            cursor.execute(text, (user["username"], user["email"], hash_password))
            connection.commit()
            message = {"message": "User created successful."}
            return message
        except psycopg2.DatabaseError as e:
            connection.rollback()
            connection.close()
            raise InternalServerError(description="Database Error: {}".format(str(e)))
        finally:
            cursor.close()
            connection.close()