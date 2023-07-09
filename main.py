from PyQt5.QtWidgets import QApplication
from aplikasi import Aplikasi
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Aplikasi()
    window.show()
    sys.exit(app.exec_())