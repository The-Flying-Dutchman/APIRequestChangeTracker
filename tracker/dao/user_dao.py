from sql_connection import SqlConnection
import pymysql.cursors

class UserDao:
    def __init__(self):
        self.connection = SqlConnection.connection

    def select_user_by_userid(self, user_id):
      with self.connection.cursor() as cursor:
            sql = "SELECT * FROM users WHERE user_id = %s"
            cursor.execute(sql, user_id)
            result = cursor.fetchall()
            return result

    def select_user_by_useremail(self, user_email):
      with self.connection.cursor() as cursor:
            sql = "SELECT * FROM users WHERE user_email = %s"
            cursor.execute(sql, user_email)
            result = cursor.fetchone()
            return result

    def select_users(self):
        with self.connection.cursor() as cursor:
            sql = "SELECT * FROM users"
            cursor.execute(sql)
            result = cursor.fetchall()
        return result

    def insert_user(self, user):
        if not user or not user.get("email") or not user.get("password"):
            return "Please pass in data"

        with self.connection.cursor() as cursor:
            sql = "INSERT INTO users (user_email, user_password) VALUES (%s, %s)"
            cursor.execute(sql, (user["email"], user["password"]))
            self.connection.commit()
            return "success"

    def update_user(self, user):
        if not user or not user.get("user_id"):
            return "Please pass in data"

        with self.connection.cursor() as cursor:
                sql = "UPDATE users SET user_email = %s, user_password = %s WHERE user_id = %s"
                cursor.execute(sql, (user["email"], user["password"], user["user_id"]))
                self.connection.commit()
                return "success"

    def delete_user_by_userid(self, user_id):
        if user_id:
            with self.connection.cursor() as cursor:
                sql = "DELETE FROM users WHERE user_id = %s"
                cursor.execute(sql, user_id)
                self.connection.commit()
                return "success"
        else:
            return "Please pass in user id"

#user_dao = UserDao()
#print user_dao.select_user_by_useremail("hello")