import pymysql

def connect():
    connection = pymysql.connect(
        host='localhost',
        user='your_username',
        password='your_password',
        database='your_database_name'
    )
    return connection
