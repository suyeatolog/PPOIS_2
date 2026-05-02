# from PySide6.QtWidgets import QMessageBox
from src.model import SolarSystemModel
from src.ui.main_view import MainView
from src.ui.show_bodies_dialog import ShowBodiesDialog
from src.ui.control_spacecraft_dialog import ControlSpacecraftDialog

class MainController:
    def __init__(self):
        self.model = SolarSystemModel()
        self.view = MainView()

        self.view.showBtn.clicked.connect(self.on_show_bodies)
        self.view.celestialCtrlBtn.clicked.connect(self.on_manage_bodies)
        self.view.spaceshipCtrlBtn.clicked.connect(self.on_control_spacecraft)
        self.view.exitBtn.clicked.connect(self.on_exit)

        self.view.set_current_body_name("Sun")
        self.view.show()

    def on_show_bodies(self):
        dialog = ShowBodiesDialog(self.model)
        dialog.exec()

    def on_manage_bodies(self):
        print("Manage bodies clicked")

    def on_control_spacecraft(self):
        dialog = ControlSpacecraftDialog(self.model, self.view)
        dialog.exec()

    def on_exit(self):
        self.view.close()