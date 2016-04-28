from tracker.dao.sql_connection import SqlConnection
import pymysql.cursors

class Crawler:
    def __init__(self):
        self.connection = SqlConnection.connection
        
    def perform_requests(self):
        return "test"
    

crawler = Crawler()
print crawler.perform_requests()