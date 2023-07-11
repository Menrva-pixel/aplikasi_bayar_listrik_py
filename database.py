import mysql.connector

class Database:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="app_listrik"
        )
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Users (
                            user_id INT PRIMARY KEY AUTO_INCREMENT,
                            username VARCHAR(255) NOT NULL,
                            password VARCHAR(255) NOT NULL,
                            privilege ENUM('Administrator', 'Pelanggan') NOT NULL)''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS ElectricityUsage (
                            usage_id INT PRIMARY KEY AUTO_INCREMENT,
                            user_id INT NOT NULL,
                            month INT NOT NULL,
                            year INT NOT NULL,
                            usage_amount DECIMAL(10, 2) NOT NULL,
                            FOREIGN KEY (user_id) REFERENCES Users(user_id))''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS ElectricityBill (
                            bill_id INT PRIMARY KEY AUTO_INCREMENT,
                            usage_id INT NOT NULL,
                            month INT NOT NULL,
                            year INT NOT NULL,
                            amount DECIMAL(10, 2) NOT NULL,
                            FOREIGN KEY (usage_id) REFERENCES ElectricityUsage(usage_id))''')

    def add_user(self, username, password, privilege):
        query = "INSERT INTO Users (username, password, privilege) VALUES (%s, %s, %s)"
        values = (username, password, privilege)
        self.cursor.execute(query, values)
        self.conn.commit()

    def get_user(self, username):
        query = "SELECT * FROM Users WHERE username = %s"
        values = (username,)
        self.cursor.execute(query, values)
        return self.cursor.fetchone()

    def get_all_users(self):
        query = "SELECT * FROM Users"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def update_user(self, user_id, username, password, privilege):
        query = "UPDATE Users SET username = %s, password = %s, privilege = %s WHERE user_id = %s"
        values = (username, password, privilege, user_id)
        self.cursor.execute(query, values)
        self.conn.commit()

    def delete_user(self, username):
        query = "DELETE FROM Users WHERE username = %s"
        values = (username,)
        self.cursor.execute(query, values)
        self.conn.commit()

    def get_electricity_usage(self, user_id):
        query = "SELECT * FROM ElectricityUsage WHERE user_id = %s"
        values = (user_id,)
        self.cursor.execute(query, values)
        return self.cursor.fetchall()

    def get_electricity_bill(self, user_id):
        query = "SELECT * FROM ElectricityBill WHERE usage_id IN " \
                "(SELECT usage_id FROM ElectricityUsage WHERE user_id = %s)"
        values = (user_id,)
        self.cursor.execute(query, values)
        return self.cursor.fetchall()

    # TODO: Tambahkan fungsi lain untuk operasi database yang diperlukan

    def close(self):
        self.conn.close()
