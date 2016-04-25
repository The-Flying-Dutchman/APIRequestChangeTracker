from sql_connection import SqlConnection
import pymysql.cursors

class RequestMetaDao:
    def __init__(self):
        self.connection = SqlConnection.connection
        
    def insert_request_meta(self, requestmeta):
        if not requestmeta or not requestmeta.get("data_request_id") or not requestmeta.get("data_content"):
            return "Please pass in data"

        with self.connection.cursor() as cursor:
            sql = "INSERT INTO request_data (data_request_id, data_content) VALUES (%s, %s)"
            cursor.execute(sql, (requestmeta["data_request_id"], requestmeta["data_content"]))
            self.connection.commit()
            return "success"

    def delete_request_meta(self, requestmetaid):
        if requestmetaid:
            with self.connection.cursor() as cursor:
                sql = "DELETE FROM request_data WHERE data_id = %s"
                cursor.execute(sql, requestmetaid)
                self.connection.commit()
                return "success"
        else:
            return "Please pass in request data id"
    
    def select_request_meta_by_requestid(self, requestid):
        if requestid:
            with self.connection.cursor() as cursor:
                sql = "SELECT * FROM request_data WHERE data_request_id = %s"
                cursor.execute(sql, requestid)
                result = cursor.fetchall()
                return result
        else:
            return "Please pass in request id"
    
    def select_request_meta_by_requestmetaid(self, requestmetaid):
        if requestmetaid:
            with self.connection.cursor() as cursor:
                sql = "SELECT * FROM request_data WHERE data_id = %s"
                cursor.execute(sql, requestmetaid)
                result = cursor.fetchall()
                return result
        else:
            return "Please pass in request data id"