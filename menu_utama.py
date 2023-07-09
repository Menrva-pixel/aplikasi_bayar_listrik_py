from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QHBoxLayout, QFrame
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt
import database

class MenuUtamaWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Menu Utama")
        self.setGeometry(200, 200, 400, 300)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Header Section
        header_layout = QHBoxLayout()

        profile_frame = QFrame()
        profile_frame.setFrameShape(QFrame.StyledPanel)
        profile_frame.setFixedHeight(80)
        profile_layout = QHBoxLayout(profile_frame)

        profile_label = QLabel("Profile Picture")
        profile_label.setFixedSize(60, 60)
        profile_label.setAlignment(Qt.AlignCenter)
        profile_layout.addWidget(profile_label)

        id_label = QLabel("ID Pengguna: ")
        id_label.setFont(QFont("Arial", 12, QFont.Bold))
        profile_layout.addWidget(id_label)

        header_layout.addWidget(profile_frame)

        header_label = QLabel("Menu Utama")
        header_label.setFont(QFont("Arial", 16, QFont.Bold))
        header_layout.addWidget(header_label)

        layout.addLayout(header_layout)

        # Penggunaan Listrik Section
        penggunaan_layout = QVBoxLayout()

        penggunaan_label = QLabel("Penggunaan Listrik")
        penggunaan_label.setFont(QFont("Arial", 14, QFont.Bold))
        penggunaan_layout.addWidget(penggunaan_label)

        # Retrieve penggunaan listrik from the database
        penggunaan_listrik = self.get_penggunaan_listrik()
        for penggunaan in penggunaan_listrik:
            penggunaan_item = QLabel(f"Bulan: {penggunaan['bulan']}, Tahun: {penggunaan['tahun']}, Tagihan: {penggunaan['tagihan']}")
            penggunaan_layout.addWidget(penggunaan_item)

        layout.addLayout(penggunaan_layout)

        self.central_widget.setLayout(layout)

    def get_penggunaan_listrik(self):
        connection = database.connect()

        try:
            with connection.cursor() as cursor:
                sql_select = "SELECT * FROM penggunaan_listrik"
                cursor.execute(sql_select)
                result = cursor.fetchall()

                return result

        finally:
            connection.close()

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = MenuUtamaWindow()
    window.show()
    sys.exit(app.exec_())
