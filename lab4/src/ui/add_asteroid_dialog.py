from PySide6.QtWidgets import QDialog, QMessageBox, QFileDialog
from PySide6.QtGui import QDoubleValidator
from ..uistransformed.addasteroid import Ui_Dialog
from solar_system_simulator import Asteroid


class AddAsteroidDialog(QDialog, Ui_Dialog):
    def __init__(self, model):
        super().__init__()
        self.setupUi(self)
        self.model = model

        self.image_path = None

        self.compositionBox.addItems(["rocky", "metallic", "carbonaceous"])
        self.orbitTypeBox.addItems([
            "main belt", "near-earth", "trojan", "centaur", "trans-neptunian"
        ])

        validator = QDoubleValidator()
        self.massEdit.setValidator(validator)
        self.xEdit.setValidator(validator)
        self.yEdit.setValidator(validator)
        self.zEdit.setValidator(validator)
        self.radiusEdit.setValidator(validator)

        self.addAsteroidBtn.clicked.connect(self.on_add_clicked)
        self.selectImageBtn.clicked.connect(self.open_image_dialog)
        self.exitBtn.clicked.connect(self.close)

    def open_image_dialog(self):
        # Диалог для выбора изображения
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Select Image",
            "",
            "Images (*.png *.jpg *.jpeg *.bmp)"
        )
        if file_path:
            self.image_path = file_path

    def on_add_clicked(self):
        name = self.nameEdit.text().strip()
        composition = self.compositionBox.currentText()
        orbit_type = self.orbitTypeBox.currentText()

        mass_text = self.massEdit.text().strip()
        x_text = self.xEdit.text().strip()
        y_text = self.yEdit.text().strip()
        z_text = self.zEdit.text().strip()
        radius_text = self.radiusEdit.text().strip()

        if not name:
            QMessageBox.warning(self, "Error", "Name cannot be empty.")
            return

        try:
            mass = float(mass_text)
            if mass <= 0:
                raise ValueError("Mass must be positive.")
        except ValueError:
            QMessageBox.warning(self, "Error", "Mass must be a positive number.")
            return

        try:
            x = float(x_text)
        except ValueError:
            QMessageBox.warning(self, "Error", "X coordinate must be a number.")
            return

        try:
            y = float(y_text)
        except ValueError:
            QMessageBox.warning(self, "Error", "Y coordinate must be a number.")
            return

        try:
            z = float(z_text)
        except ValueError:
            QMessageBox.warning(self, "Error", "Z coordinate must be a number.")
            return

        try:
            radius = float(radius_text)
            if radius <= 0:
                raise ValueError("Radius must be positive.")
        except ValueError:
            QMessageBox.warning(self, "Error", "Radius must be a positive number.")
            return

        asteroid = Asteroid(composition=composition, orbit_type=orbit_type)
        asteroid.name = name
        asteroid.mass = mass
        asteroid.position = (x, y, z)
        asteroid.radius = radius

        if self.image_path:
            asteroid.image_path = self.image_path

        self.model.solar_system.add_body(asteroid)

        from src.model import OBJECT_TO_IMAGE
        OBJECT_TO_IMAGE[name] = self.image_path

        QMessageBox.information(self, "Success", f"Asteroid '{name}' added successfully.")
        self.accept()