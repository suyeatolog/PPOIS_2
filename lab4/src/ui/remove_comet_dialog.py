from PySide6.QtWidgets import QDialog, QMessageBox
from ..uistransformed.removecomet import Ui_Dialog
from solar_system_simulator import Comet


class RemoveCometDialog(QDialog, Ui_Dialog):
    def __init__(self, model, main_view):
        super().__init__()
        self.setupUi(self)
        self.model = model
        self.main_view = main_view

        self.populate_comets_box()

        self.removeCometBtn.clicked.connect(self.on_remove_clicked)
        self.exitBtn.clicked.connect(self.close)

    def populate_comets_box(self):
        self.cometsBox.clear()
        comets = self.model.solar_system.get_comets()
        for comet in comets:
            self.cometsBox.addItem(comet.name)

    def on_remove_clicked(self):
        selected_name = self.cometsBox.currentText()
        if not selected_name:
            QMessageBox.warning(self, "Error", "No comet selected.")
            return

        comet = self.model.get_body_by_name(selected_name)
        if not comet or not isinstance(comet, Comet):
            QMessageBox.warning(self, "Error", "Could not find comet.")
            return

        self.model.solar_system.remove_body(comet)

        from src.model import OBJECT_TO_IMAGE
        OBJECT_TO_IMAGE.pop(selected_name, None)

        if self.model.current_body and self.model.current_body.name == selected_name:
            self.model.current_body = self.model.solar_system.sun
            self.main_view.set_current_body_name("default")

        QMessageBox.information(self, "Success", f"Comet '{selected_name}' removed successfully.")
        self.populate_comets_box()