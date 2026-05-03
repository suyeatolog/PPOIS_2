from PySide6.QtWidgets import QDialog
from ..uistransformed.addorremove import Ui_Dialog
from .add_asteroid_dialog import AddAsteroidDialog
from .add_comet_dialog import AddCometDialog
from .add_satellite_dialog import AddSatelliteDialog 
from .remove_asteroid_dialog import RemoveAsteroidDialog
from .remove_comet_dialog import RemoveCometDialog
from .remove_satellite_dialog import RemoveSatelliteDialog


class AddRemoveDialog(QDialog, Ui_Dialog):
    def __init__(self, model, main_view):
        super().__init__()
        self.setupUi(self)
        self.model = model
        self.main_view = main_view

        self.addAsteroidBtn.clicked.connect(self.open_add_asteroid)
        self.addCometBtn.clicked.connect(self.open_add_comet)
        self.addSatelliteBtn.clicked.connect(self.open_add_satellite)
        self.removeAsteroidBtn.clicked.connect(self.open_remove_asteroid)
        self.removeCometBtn.clicked.connect(self.open_remove_comet)       
        self.removeSatelliteBtn.clicked.connect(self.open_remove_satellite)
        self.exit2Btn.clicked.connect(self.close)

    def open_add_asteroid(self):
        dialog = AddAsteroidDialog(self.model)
        dialog.exec()

    def open_add_comet(self):
        dialog = AddCometDialog(self.model)
        dialog.exec()

    def open_add_satellite(self):
        dialog = AddSatelliteDialog(self.model)
        dialog.exec()

    def open_remove_asteroid(self):
        dialog = RemoveAsteroidDialog(self.model, self.main_view)
        dialog.exec()

    def open_remove_comet(self):
        dialog = RemoveCometDialog(self.model, self.main_view)
        dialog.exec()

    def open_remove_satellite(self):
        dialog = RemoveSatelliteDialog(self.model, self.main_view)
        dialog.exec()