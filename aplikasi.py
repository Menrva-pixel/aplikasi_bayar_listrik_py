from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from register import register

import auth
import register

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

        register_button = QPushButton("Register")
        layout.addWidget(register_button)
        register_button.clicked.connect(self.show_register)

        self.login_widget.setLayout(layout)

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        auth.login(username, password)

    def show_register(self):
        self.register_widget = QWidget()
        self.setCentralWidget(self.register_widget)

        layout = QVBoxLayout()

        label = QLabel("Registrasi Pengguna Baru")
        label.setAlignment(Qt.AlignCenter)
        label.setFont(QFont("Arial", 16))
        layout.addWidget(label)

        nama_label = QLabel("Nama:")
        layout.addWidget(nama_label)

        self.nama_input = QLineEdit()
        layout.addWidget(self.nama_input)

        alamat_label = QLabel("Alamat:")
        layout.addWidget(alamat_label)

        self.alamat_input = QLineEdit()
        layout.addWidget(self.alamat_input)

        email_label = QLabel("Email:")
        layout.addWidget(email_label)

        self.email_input = QLineEdit()
        layout.addWidget(self.email_input)

        telepon_label = QLabel("Telepon:")
        layout.addWidget(telepon_label)

        self.telepon_input = QLineEdit()
        layout.addWidget(self.telepon_input)

        register_button = QPushButton("Register")
        layout.addWidget(register_button)
        register_button.clicked.connect(self.register)

        back_button = QPushButton("Kembali")
        layout.addWidget(back_button)
        back_button.clicked.connect(self.back_to_login)

        self.register_widget.setLayout(layout)

    def register(self):
        nama = self.nama_input.text()
        alamat = self.alamat_input.text()
        email = self.email_input.text()
        telepon = self.telepon_input.text()

        password = self.password_input.text()  # Simpan nilai password sebelum menghapus widget

        # Hapus widget dan persiapkan tampilan login
        self.register_widget.deleteLater()
        self.setCentralWidget(self.login_widget)

        register.register(nama, alamat, email, telepon, password)
        self.clear_input_fields()
        self.init_login_ui()

    def clear_input_fields(self):
        self.username_input.clear()
        self.password_input.clear()
        self.nama_input.clear()
        self.alamat_input.clear()
        self.email_input.clear()
        self.telepon_input.clear()

    def back_to_login(self):
        self.init_login_ui()

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = Aplikasi()
    window.show()
    sys.exit(app.exec_())
