from sql_connection import SqlConnection
import pymysql.cursors

class Request:
    def __init__(self):
        self.connection = SqlConnection.connection
        
    def perform_requests(self):
        return "test"
    

request = Request()
print request.perform_requests()