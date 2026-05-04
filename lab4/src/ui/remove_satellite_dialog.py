from PySide6.QtWidgets import QDialog, QMessageBox
from ..uistransformed.removesatellite import Ui_Dialog
from solar_system_simulator import Satellite


class RemoveSatelliteDialog(QDialog, Ui_Dialog):
    def __init__(self, model, main_view):
        super().__init__()
        self.setupUi(self)
        self.model = model
        self.main_view = main_view

        self.populate_satellites_box()

        self.removeSatelliteBtn.clicked.connect(self.on_remove_clicked)
        self.exitBtn.clicked.connect(self.close)

    def populate_satellites_box(self):
        self.satellitesBox.clear()
        satellites = self.model.solar_system.get_satellites()
        for satellite in satellites:
            self.satellitesBox.addItem(satellite.name)

    def on_remove_clicked(self):
        selected_name = self.satellitesBox.currentText()
        if not selected_name:
            QMessageBox.warning(self, "Error", "No satellite selected.")
            return

        satellite = self.model.get_body_by_name(selected_name)
        if not satellite or not isinstance(satellite, Satellite):
            QMessageBox.warning(self, "Error", "Could not find satellite.")
            return

        self.model.solar_system.remove_body(satellite)

        from src.model import OBJECT_TO_IMAGE
        OBJECT_TO_IMAGE.pop(selected_name, None)

        if self.model.current_body and self.model.current_body.name == selected_name:
            self.model.current_body = self.model.solar_system.sun
            self.main_view.set_current_body_name("default")

        QMessageBox.information(self, "Success", f"Satellite '{selected_name}' removed successfully.")
        self.populate_satellites_box()