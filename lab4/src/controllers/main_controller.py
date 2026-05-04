from src.model import SolarSystemModel
from src.ui.main_view import MainView
from src.ui.show_bodies_dialog import ShowBodiesDialog
from src.ui.control_spacecraft_dialog import ControlSpacecraftDialog
from src.ui.add_remove_dialog import AddRemoveDialog

class MainController:
    def __init__(self):
        self.model = SolarSystemModel()
        self.view = MainView()

        self.view.showBtn.clicked.connect(self.on_show_bodies)
        self.view.celestialCtrlBtn.clicked.connect(self.on_manage_bodies)
        self.view.spaceshipCtrlBtn.clicked.connect(self.on_control_spacecraft)
        self.view.exitBtn.clicked.connect(self.on_exit)

        self.view.set_current_body_name("default")
        self.view.show()

    def on_show_bodies(self):
        dialog = ShowBodiesDialog(self.model)
        dialog.exec()

    def on_manage_bodies(self):
        dialog = AddRemoveDialog(self.model, self.view)
        dialog.exec()

    def on_control_spacecraft(self):
        dialog = ControlSpacecraftDialog(self.model, self.view)
        dialog.exec()

    def on_exit(self):
        self.view.close()