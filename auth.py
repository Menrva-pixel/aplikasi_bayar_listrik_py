import bcrypt
import database

def login(email, password):
    connection = database.connect()

    try:
        with connection.cursor() as cursor:
            sql = "SELECT password FROM pelanggan WHERE email = %s"
            cursor.execute(sql, (email,))
            result = cursor.fetchone()

            if result:
                stored_password = result[0]
                if bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8')):
                    print("Login successful")
                elif bcrypt.checkpw(password.encode('utf-8'), bcrypt.hashpw(stored_password.encode('utf-8'), bcrypt.gensalt())):
                    # If the stored password is not hashed with the current bcrypt version, rehash the password
                    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
                    sql_update = "UPDATE pelanggan SET password = %s WHERE email = %s"
                    cursor.execute(sql_update, (hashed_password, email))
                    connection.commit()
                    print("Login successful (password rehashed)")
                else:
                    print("Invalid email or password")
            else:
                print("Invalid email or password")

    finally:
        connection.close()
