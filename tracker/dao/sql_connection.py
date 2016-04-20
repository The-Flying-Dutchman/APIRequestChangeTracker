import pymysql
from tracker import *

class SqlConnection:
    connection = pymysql.connect(host=app.config["DB_HOST"],
                             user=app.config["DB_USERNAME"],
                             password=app.config["DB_PASSWORD"],
                             db='api_tracker',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)





