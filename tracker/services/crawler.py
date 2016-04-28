import requests
import pymysql

DB_HOST = "162.243.65.63"
DB_USERNAME = "root"
DB_PASSWORD = "weisql"

class SqlConnection:
    connection = pymysql.connect(host=DB_HOST,
                                 user=DB_USERNAME,
                                 password=DB_PASSWORD,
                                 db='api_tracker',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)

class Crawler:
    def __init__(self):
        self.connection = SqlConnection.connection

    def perform_requests(self):
        with self.connection.cursor() as cursor:
            sql = "SELECT * FROM request_record WHERE request_last_execute IS NULL OR DATE_ADD(request_last_execute, INTERVAL request_interval HOUR) <  NOW()"
            cursor.execute(sql)
            for row in cursor:
                URL = row["request_url"]
                ID = row["request_id"]
                if URL:
                    url = URL
                    data = '{}'
                    response = requests.get(url, data=data)
                    sql2 = "SELECT * FROM request_data WHERE data_request_id = %s ORDER BY data_timestamp DESC LIMIT 1"
                    cursor.execute(sql2, ID)
                    ROW = cursor.fetchone()
                    if ROW:
                        CONTENT = ROW["data_content"]
                        if CONTENT != response.text:
                            with self.connection.cursor() as cursor:
                                sql = "INSERT INTO request_data (data_request_id, data_content) VALUES (%s, %s)"
                                cursor.execute(sql, (ID, response.text))
                                self.connection.commit()
                    else:
                        with self.connection.cursor() as cursor:
                            sql = "INSERT INTO request_data (data_request_id, data_content) VALUES (%s, %s)"
                            cursor.execute(sql, (ID, response.text))
                            self.connection.commit()
            
        return ""

crawler = Crawler()
crawler.perform_requests()