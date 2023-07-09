from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt
import auth
from menu_utama import MenuUtamaWindow  

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Aplikasi Pembayaran Listrik")
        self.setGeometry(200, 200, 400, 300)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        logo_label = QLabel()
        logo_pixmap = QPixmap("logo.png")  
        logo_label.setPixmap(logo_pixmap)
        logo_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(logo_label)

        title_label = QLabel("Selamat Datang")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setFont(QFont("Arial", 16, QFont.Bold))
        layout.addWidget(title_label)

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

        register_label = QLabel("Belum punya akun?")
        register_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(register_label)

        register_button = QPushButton("Register")
        layout.addWidget(register_button)
        register_button.clicked.connect(self.show_register)

        self.central_widget.setLayout(layout)

    def login(self):
        nama = self.username_input.text()
        password = self.password_input.text()
      
        if auth.login(nama, password):
            self.menu_utama = MenuUtamaWindow()
            self.menu_utama.show()
            self.hide()

    def show_register(self):
        print("Register clicked")
 

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec_())
