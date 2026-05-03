from PySide6.QtWidgets import QDialog, QMessageBox, QFileDialog
from PySide6.QtGui import QIntValidator
from ..uistransformed.addsatellite import Ui_Dialog
from solar_system_simulator import Satellite


class AddSatelliteDialog(QDialog, Ui_Dialog):
    def __init__(self, model):
        super().__init__()
        self.setupUi(self)
        self.model = model

        self.image_path = None

        validator = QIntValidator()
        self.orbitalEdit.setValidator(validator)
        self.distanceEdit.setValidator(validator)
        self.massEdit.setValidator(validator)
        self.xEdit.setValidator(validator)
        self.yEdit.setValidator(validator)
        self.zEdit.setValidator(validator)
        self.radiusEdit.setValidator(validator)

        self.populate_planet_box()

        self.addSatelliteBtn.clicked.connect(self.on_add_clicked)
        self.exitBtn.clicked.connect(self.close)

        if hasattr(self, 'selectImageBtn'):
            self.selectImageBtn.clicked.connect(self.open_image_dialog)

    def populate_planet_box(self):
        planets = self.model.solar_system.get_planets()
        for planet in planets:
            self.planetBox.addItem(planet.name)

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
        orbited_planet = self.planetBox.currentText()

        orbital_period_text = self.orbitalEdit.text().strip()
        distance_text = self.distanceEdit.text().strip()
        mass_text = self.massEdit.text().strip()
        x_text = self.xEdit.text().strip()
        y_text = self.yEdit.text().strip()
        z_text = self.zEdit.text().strip()
        radius_text = self.radiusEdit.text().strip()

        if not name:
            QMessageBox.warning(self, "Error", "Name cannot be empty.")
            return

        if not orbited_planet:
            QMessageBox.warning(self, "Error", "Orbited planet must be selected.")
            return

        try:
            orbital_period = int(orbital_period_text)
            if orbital_period <= 0:
                raise ValueError("Orbital period must be positive.")
        except ValueError:
            QMessageBox.warning(self, "Error", "Orbital period must be a positive integer.")
            return

        try:
            distance = int(distance_text)
            if distance <= 0:
                raise ValueError("Distance must be positive.")
        except ValueError:
            QMessageBox.warning(self, "Error", "Distance must be a positive integer.")
            return

        try:
            mass = int(mass_text)
            if mass <= 0:
                raise ValueError("Mass must be positive.")
        except ValueError:
            QMessageBox.warning(self, "Error", "Mass must be a positive integer.")
            return

        try:
            x = int(x_text)
        except ValueError:
            QMessageBox.warning(self, "Error", "X coordinate must be an integer.")
            return

        try:
            y = int(y_text)
        except ValueError:
            QMessageBox.warning(self, "Error", "Y coordinate must be an integer.")
            return

        try:
            z = int(z_text)
        except ValueError:
            QMessageBox.warning(self, "Error", "Z coordinate must be an integer.")
            return

        try:
            radius = int(radius_text)
            if radius <= 0:
                raise ValueError("Radius must be positive.")
        except ValueError:
            QMessageBox.warning(self, "Error", "Radius must be a positive integer.")
            return

        satellite = Satellite(orbited_planet=orbited_planet, orbital_period=orbital_period, distance_from_planet=distance)
        satellite.name = name
        satellite.mass = mass
        satellite.position = (x, y, z)
        satellite.radius = radius

        if self.image_path:
            satellite.image_path = self.image_path

        self.model.solar_system.add_body(satellite)

        from src.model import OBJECT_TO_IMAGE
        OBJECT_TO_IMAGE[name] = self.image_path

        QMessageBox.information(self, "Success", f"Satellite '{name}' added successfully.")
        self.accept()