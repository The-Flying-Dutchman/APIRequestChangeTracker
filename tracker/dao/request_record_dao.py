from sql_connection import SqlConnection
import pymysql.cursors


class RequestRecordDao:
    def __init__(self):
        self.connection = SqlConnection.connection

    def insert_request_record(self, request_record):
        if not request_record or not request_record.get("user_id") or not request_record.get(
                "request_url") or not request_record.get("request_interval"):
            return "Please pass in data"

        with self.connection.cursor() as cursor:
            sql = "INSERT INTO request_record (request_user_id, request_url, request_interval) VALUES (%s, %s, %s)"
            cursor.execute(sql, (
            request_record["user_id"], request_record["request_url"], request_record["request_interval"]))
            self.connection.commit()
            return "success"

            # return data_id

    def select_request_record_by_requestid(self, request_id):
        with self.connection.cursor() as cursor:
            sql = "SELECT * FROM request_record WHERE request_id = %s"
            cursor.execute(sql, request_id)
            result = cursor.fetchall()
            return result

    def select_request_record(self):
        with self.connection.cursor() as cursor:
            sql = "SELECT * FROM request_record"
            cursor.execute(sql)
            result = cursor.fetchall()
        return result

    def select_request_record_by_userid(self, userid):
        with self.connection.cursor() as cursor:
            sql = "SELECT * FROM request_record WHERE request_user_id = %s"
            cursor.execute(sql, userid)
            result = cursor.fetchall()
            return result

    def update_request(self, request_record):
        if not request_record or not request_record.get("request_id") or not request_record.get(
                "request_url") or not request_record.get("request_interval"):
            return "Please pass in data"

        with self.connection.cursor() as cursor:
            sql = "UPDATE request_record SET request_url = %s, request_interval = %s WHERE request_id = %s"
            cursor.execute(sql, (
            request_record["request_url"], request_record["request_interval"], request_record["request_id"]))
            self.connection.commit()
            return "success"

    def delete_request_by_requestid(self, request_id):
        if request_id:
            with self.connection.cursor() as cursor:
                sql = "DELETE FROM request_record WHERE request_id = %s"
                cursor.execute(sql, request_id)
                self.connection.commit()
                return "success"
        else:
            return "Please pass in request id"
