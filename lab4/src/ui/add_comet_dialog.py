from PySide6.QtWidgets import QDialog, QMessageBox, QFileDialog
from PySide6.QtGui import QDoubleValidator
from PySide6.QtCore import QLocale
from ..uistransformed.addcomet import Ui_Dialog
from solar_system_simulator import Comet


class AddCometDialog(QDialog, Ui_Dialog):
    def __init__(self, model):
        super().__init__()
        self.setupUi(self)
        self.model = model

        self.image_path = None

        validator = QDoubleValidator()
        validator.setLocale(QLocale(QLocale.C))
        
        self.coreDiameterEdit.setValidator(validator)
        self.orbitalPeriodEdit.setValidator(validator)
        self.eccentricityEdit.setValidator(validator)
        self.massEdit.setValidator(validator)
        self.xEdit.setValidator(validator)
        self.yEdit.setValidator(validator)
        self.zEdit.setValidator(validator)
        self.radiusEdit.setValidator(validator)

        self.addCometBtn_2.clicked.connect(self.on_add_clicked)
        self.exitBtn.clicked.connect(self.close)

        if hasattr(self, 'selectImageBtn'):
            self.selectImageBtn.clicked.connect(self.open_image_dialog)

    def open_image_dialog(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Select Image",
            "",
            "Images (*.png *.jpg *.jpeg *.gif *.bmp)"
        )
        if file_path:
            self.image_path = file_path

    def on_add_clicked(self):
        name = self.nameEdit.text().strip()

        core_diameter_text = self.coreDiameterEdit.text().strip()
        orbital_period_text = self.orbitalPeriodEdit.text().strip()
        eccentricity_text = self.eccentricityEdit.text().strip()
        mass_text = self.massEdit.text().strip()
        x_text = self.xEdit.text().strip()
        y_text = self.yEdit.text().strip()
        z_text = self.zEdit.text().strip()
        radius_text = self.radiusEdit.text().strip()

        if not name:
            QMessageBox.warning(self, "Error", "Name cannot be empty.")
            return

        try:
            core_diameter = float(core_diameter_text)
            if core_diameter <= 0:
                raise ValueError("Core diameter must be positive.")
        except ValueError:
            QMessageBox.warning(self, "Error", "Core diameter must be a positive number.")
            return

        try:
            orbital_period = float(orbital_period_text)
            if orbital_period <= 0:
                raise ValueError("Orbital period must be positive.")
        except ValueError:
            QMessageBox.warning(self, "Error", "Orbital period must be a positive number.")
            return

        try:
            eccentricity = float(eccentricity_text)
            if eccentricity < 0 or eccentricity > 1:
                raise ValueError("Eccentricity must be between 0 and 1.")
        except ValueError:
            QMessageBox.warning(self, "Error", "Eccentricity must be a number between 0 and 1.")
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

        comet = Comet(core_diameter=core_diameter, period=orbital_period, eccentricity=eccentricity)
        comet.name = name
        comet.mass = mass
        comet.position = (x, y, z)
        comet.radius = radius

        if self.image_path:
            comet.image_path = self.image_path

        self.model.solar_system.add_body(comet)

        from src.model import OBJECT_TO_IMAGE
        OBJECT_TO_IMAGE[name] = self.image_path

        QMessageBox.information(self, "Success", f"Comet '{name}' added successfully.")
        self.accept()