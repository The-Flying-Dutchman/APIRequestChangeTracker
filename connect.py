import pymysql.cursors
import pymysql

connection = pymysql.connect(host='162.243.65.63',
    user='root',
    password='weisql',
    db='api_tracker',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor)

def users(method, data = ""):
    if method == "GET":
        if not data:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM users"
                cursor.execute(sql)
                result = cursor.fetchall()
                return result
        else:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM users WHERE user_id = %s"
                cursor.execute(sql, data)
                result = cursor.fetchall()
                return result
    elif method == "POST":
        if not data or not data.get("email") or not data.get("password"):
            return "Please pass in data"
        else:
            with connection.cursor() as cursor:
                sql = "INSERT INTO users (user_email, user_password) VALUES (%s, %s)"
                cursor.execute(sql, (data["email"], data["password"]))
                connection.commit()
                return "User inserted"
    elif method == "PUT":
        if data:
            with connection.cursor() as cursor:
                sql = "UPDATE users SET user_email = %s, user_password = %s WHERE user_id = %s"
                cursor.execute(sql, (data["email"], data["password"], data["user_id"]))
                connection.commit()
                return "User updated"
        else:
            return "Please pass in data"
        return
    elif method == "DELETE":
        if data:
            with connection.cursor() as cursor:
                sql = "DELETE FROM users WHERE user_id = %s"
                cursor.execute(sql, data)
                connection.commit()
                return "User deleted"
        else:
            return "Please pass in user id"
    return

print(users("GET"))
print(users("GET", 1))
print(users("POST", {"email": "bob", "password": "bob2"}))
print(users("DELETE", 9))
print(users("PUT", {"email": "billy", "password": "billy", "user_id": 1}))