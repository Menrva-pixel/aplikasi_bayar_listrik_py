from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from database import connect

class Aplikasi(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Aplikasi Pembayaran Listrik Pascabayar")
        self.setGeometry(200, 200, 400, 300)

        self.login_widget = QWidget()
        self.setCentralWidget(self.login_widget)

        self.init_login_ui()

    def init_login_ui(self):
        layout = QVBoxLayout()

        label = QLabel("Masuk ke Akun Anda")
        label.setAlignment(Qt.AlignCenter)
        label.setFont(QFont("Arial", 16))
        layout.addWidget(label)

        username_label = QLabel("Username:")
        layout.addWidget(username_label)

        self.username_input = QLineEdit()
        layout.addWidget(self.username_input)

        password_label = QLabel("Password:")
        layout.addWidget(password_label)

        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.password_input)

        login_button = QPushButton("Login")
        layout.addWidget(login_button)
        login_button.clicked.connect(self.login)

        self.login_widget.setLayout(layout)

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        connection = connect()

        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM users WHERE username = %s AND password = %s"
                cursor.execute(sql, (username, password))
                result = cursor.fetchone()

                if result:
                    print("Login successful")
                else:
                    print("Invalid username or password")

        finally:
            connection.close()
