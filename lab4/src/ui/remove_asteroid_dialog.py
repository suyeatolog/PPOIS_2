from PySide6.QtWidgets import QDialog, QMessageBox
from ..uistransformed.removeasteroid import Ui_Dialog
from solar_system_simulator import Asteroid


class RemoveAsteroidDialog(QDialog, Ui_Dialog):
    def __init__(self, model, main_view):
        super().__init__()
        self.setupUi(self)
        self.model = model
        self.main_view = main_view

        self.populate_asteroids_box()

        self.removeAsteroidBtn.clicked.connect(self.on_remove_clicked)
        self.exitBtn.clicked.connect(self.close)

    def populate_asteroids_box(self):
        self.asteroidsBox.clear()
        asteroids = self.model.solar_system.get_asteroids()
        for asteroid in asteroids:
            self.asteroidsBox.addItem(asteroid.name)

    def on_remove_clicked(self):
        selected_name = self.asteroidsBox.currentText()
        if not selected_name:
            QMessageBox.warning(self, "Error", "No asteroid selected.")
            return

        asteroid = self.model.get_body_by_name(selected_name)
        if not asteroid or not isinstance(asteroid, Asteroid):
            QMessageBox.warning(self, "Error", "Could not find asteroid.")
            return

        self.model.solar_system.remove_body(asteroid)

        from src.model import OBJECT_TO_IMAGE
        OBJECT_TO_IMAGE.pop(selected_name, None)

        if self.model.current_body and self.model.current_body.name == selected_name:
            self.model.current_body = self.model.solar_system.sun
            self.main_view.set_current_body_name("Sun")

        QMessageBox.information(self, "Success", f"Asteroid '{selected_name}' removed successfully.")
        self.populate_asteroids_box()