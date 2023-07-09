import bcrypt
import database

def login(nama, password):
    connection = database.connect()

    try:
        with connection.cursor() as cursor:
            sql_select = "SELECT password FROM pelanggan WHERE nama = %s"
            cursor.execute(sql_select, (nama,))
            result = cursor.fetchone()

            if result:
                stored_password = result["password"]

                if bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8')):
                    print("Login successful")
                else:
                    print("Invalid password")
            else:
                print("Invalid nama")

    finally:
        connection.close()

def register(nama, alamat, email, telepon, password):
    connection = database.connect()

    try:
        with connection.cursor() as cursor:
            sql_check_nama = "SELECT COUNT(*) FROM pelanggan WHERE nama = %s"
            cursor.execute(sql_check_nama, (nama,))
            result = cursor.fetchone()

            if result["COUNT(*)"] > 0:
                print("Nama already exists")
                return

            random_password = generate_random_password()
            hashed_random_password = bcrypt.hashpw(random_password.encode('utf-8'), bcrypt.gensalt())

            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

            sql_insert = "INSERT INTO pelanggan (nama, alamat, email, telepon, password) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql_insert, (nama, alamat, email, telepon, hashed_random_password))
            connection.commit()

            print("Registration successful")
            print("Random Password:", random_password)

    finally:
        connection.close()

def generate_random_password():
    #nanti
    pass