from src.controllers.main_controller import MainController
import sys
from PySide6.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication(sys.argv)
    controller = MainController()
    sys.exit(app.exec())