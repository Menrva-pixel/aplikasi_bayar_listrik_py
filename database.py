import pymysql

def connect():
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        database='app_listrik'
    )
    return connection
