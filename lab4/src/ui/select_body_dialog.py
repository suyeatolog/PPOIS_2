from PySide6.QtWidgets import QDialog, QMessageBox
from ..uistransformed.selectbody import Ui_Dialog

class SelectBodyDialog(QDialog, Ui_Dialog):
    def __init__(self, model):
        super().__init__()
        self.setupUi(self)
        self.model = model

        self.populate_combobox()

        self.travelBtn.clicked.connect(self.on_travel_clicked)

    def populate_combobox(self):
        bodies = self.model.get_celestial_bodies_only()
        for body in bodies:
            self.bodiesBox.addItem(body.name)

    def on_travel_clicked(self):
        if not self.model.check_launch_status():
            QMessageBox.warning(self, "Warning", "Spacecraft is not launched. Cannot travel.")
            return

        selected_name = self.bodiesBox.currentText()
        target_body = self.model.get_body_by_name(selected_name)
        if target_body:
            try:
                self.model.travel_to(target_body)
            except Exception as e:
                QMessageBox.critical(self, "Error", str(e))
                return
        self.accept()