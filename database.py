import pymysql

def connect():
    connection = pymysql.connect(
        host="localhost",
        user="root",
        password="",
        database="app_listrik",
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor
    )

    return connection
