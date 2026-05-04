from PySide6.QtWidgets import QMainWindow
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
from src.model import IMAGES_DIR, OBJECT_TO_IMAGE
from src.uistransformed.mainwindow import Ui_MainWindow

class MainView(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.set_current_body_name("default")

    def set_current_body_name(self, name: str):
        self.objectNameLabel.setText(name)

        img_filename = OBJECT_TO_IMAGE.get(name)
        if img_filename:
            img_path = IMAGES_DIR / img_filename
            if img_path.exists():
                pixmap = QPixmap(str(img_path))
                pixmap = pixmap.scaledToHeight(630, Qt.SmoothTransformation)
                self.objectImageLabel.setPixmap(pixmap)
            else:
                self.objectImageLabel.setText(f"Image not found: {img_filename}")
                self.objectImageLabel.setAlignment(Qt.AlignCenter)
        else:
            self.objectImageLabel.setText(f"No image for: {name}")
            self.objectImageLabel.setAlignment(Qt.AlignCenter)