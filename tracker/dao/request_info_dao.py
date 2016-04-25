from sql_connection import SqlConnection
import pymysql.cursors

class RequestInfoDao:
    def __init__(self):
        self.connection = SqlConnection.connection
        
    def insert_request_info(self, request_info):
        if not request_info or not request_info.get("user_id") or not request_info.get("request_url") or not request_info.get("request_interval"):
            return "Please pass in data"

        with self.connection.cursor() as cursor:
            sql = "INSERT INTO requests (request_user_id, request_url, request_interval) VALUES (%s, %s, %s)"
            cursor.execute(sql, (request_info["user_id"], request_info["request_url"], request_info["request_interval"]))
            self.connection.commit()
            return "success"

    def select_request_info_by_requestid(self, requestid):
        with self.connection.cursor() as cursor:
            sql = "SELECT * FROM requests WHERE request_id = %s"
            cursor.execute(sql, requestid)
            result = cursor.fetchall()
            return result
    
    def select_requests(self):
        with self.connection.cursor() as cursor:
            sql = "SELECT * FROM requests"
            cursor.execute(sql)
            result = cursor.fetchall()
        return result

    def select_request_info_by_userid(self, userid):
        with self.connection.cursor() as cursor:
            sql = "SELECT * FROM requests WHERE request_user_id = %s"
            cursor.execute(sql, userid)
            result = cursor.fetchall()
            return result
            
    def update_request(self, request_info):
        if not request_info or not request_info.get("request_id") or not request_info.get("request_url") or not request_info.get("request_interval"):
            return "Please pass in data"

        with self.connection.cursor() as cursor:
                sql = "UPDATE requests SET request_url = %s, request_interval = %s WHERE request_id = %s"
                cursor.execute(sql, (request_info["request_url"], request_info["request_interval"], request_info["request_id"]))
                self.connection.commit()
                return "success"
    
    def delete_request_by_requestid(self, requestid):
        if requestid:
            with self.connection.cursor() as cursor:
                sql = "DELETE FROM requests WHERE request_id = %s"
                cursor.execute(sql, requestid)
                self.connection.commit()
                return "success"
        else:
            return "Please pass in request id"