import bcrypt
import database

def register(nama, alamat, email, telepon, password):
    connection = database.connect()

    try:
        with connection.cursor() as cursor:
            sql_insert = "INSERT INTO pelanggan (nama, alamat, email, telepon, password) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql_insert, (nama, alamat, email, telepon, password))
            connection.commit()

            user_id = cursor.lastrowid

            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

            sql_update = "UPDATE pelanggan SET password = %s WHERE id = %s"
            cursor.execute(sql_update, (hashed_password, user_id))
            connection.commit()

            print("Registration successful")
            print("User ID:", user_id)

    finally:
        connection.close()

def main():
    nama = input("Nama: ")
    alamat = input("Alamat: ")
    email = input("Email: ")
    telepon = input("Telepon: ")
    password = input("Password: ")

    register(nama, alamat, email, telepon, password)

if __name__ == "__main__":
    main()
