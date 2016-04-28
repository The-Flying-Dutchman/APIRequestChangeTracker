from sql_connection import SqlConnection


class RequestDataDao:
    def __init__(self):
        self.connection = SqlConnection.connection

    def insert_request_data(self, requestdata):
        if not requestdata or not requestdata.get("data_request_id") or not requestdata.get("data_content"):
            return "Please pass in data"

        with self.connection.cursor() as cursor:
            sql = "INSERT INTO request_data (data_request_id, data_content) VALUES (%s, %s)"
            cursor.execute(sql, (requestdata["data_request_id"], requestdata["data_content"]))
            self.connection.commit()
            return self.connection.insert_id()

    def delete_request_data(self, requestdataid):
        if requestdataid:
            with self.connection.cursor() as cursor:
                sql = "DELETE FROM request_data WHERE data_id = %s"
                cursor.execute(sql, requestdataid)
                self.connection.commit()
                return "success"
        else:
            return "Please pass in request data id"

    def select_request_data_by_requestid(self, requestid):
        if requestid:
            with self.connection.cursor() as cursor:
                sql = "SELECT * FROM request_data WHERE data_request_id = %s"
                cursor.execute(sql, requestid)
                result = cursor.fetchall()
                return result
        else:
            return "Please pass in request id"

    def select_request_data_by_data_id(self, data_id):
        if data_id:
            with self.connection.cursor() as cursor:
                sql = "SELECT * FROM request_data WHERE data_id = %s"
                cursor.execute(sql, data_id)
                result = cursor.fetchall()
                return result
        else:
            return "Please pass in request data id"
