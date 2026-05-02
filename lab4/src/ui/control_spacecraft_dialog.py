from PySide6.QtWidgets import QDialog, QMessageBox
from ..uistransformed.controlspacecraft import Ui_Dialog
from .select_body_dialog import SelectBodyDialog

class ControlSpacecraftDialog(QDialog, Ui_Dialog):
    def __init__(self, model, main_view):
        super().__init__()
        self.setupUi(self)
        self.model = model
        self.main_view = main_view

        self.update_fuel_display()

        self.launchBtn.clicked.connect(self.on_launch_clicked)
        self.travelBtn.clicked.connect(self.open_select_body_dialog)
        self.collectdataBtn.clicked.connect(self.on_collect_data_clicked)
        self.fuelupBtn.clicked.connect(self.on_fuel_up_clicked)
        self.exit3Btn.clicked.connect(self.close)

    def update_fuel_display(self):
        fuel = self.model.get_fuel_level()
        self.resultLabel_2.setText(f"Fuel: {fuel}")

    def on_launch_clicked(self):
        try:
            self.model.launch_spacecraft()
            QMessageBox.information(self, "Success", "Spacecraft launched successfully!")
            self.update_fuel_display()
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def open_select_body_dialog(self):
        if not self.model.check_launch_status():
            QMessageBox.warning(self, "Warning", "Spacecraft is not launched. Please launch it first.")
            return

        dialog = SelectBodyDialog(self.model)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            self.update_fuel_display()
            current_name = self.model.current_body.name
            self.main_view.set_current_body_name(current_name) 

    def on_collect_data_clicked(self):
        if not self.model.check_launch_status():
            QMessageBox.warning(self, "Warning", "Spacecraft is not launched. Cannot collect data.")
            return

        result = self.model.collect_data()
        self.resultLabel.setText(str(result))

    def on_fuel_up_clicked(self):
        self.model.fuel_up()
        self.update_fuel_display()
        QMessageBox.information(self, "Success", "Spacecraft fueled up.")