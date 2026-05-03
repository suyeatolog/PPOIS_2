from PySide6.QtWidgets import QDialog
from ..uistransformed.addorremove import Ui_Dialog
from .add_asteroid_dialog import AddAsteroidDialog
from .add_comet_dialog import AddCometDialog
from .add_satellite_dialog import AddSatelliteDialog 


class AddRemoveDialog(QDialog, Ui_Dialog):
    def __init__(self, model):
        super().__init__()
        self.setupUi(self)
        self.model = model

        self.addAsteroidBtn.clicked.connect(self.open_add_asteroid)
        self.addCometBtn.clicked.connect(self.on_add_comet_clicked)
        self.addSatelliteBtn.clicked.connect(self.on_add_satellite_clicked)
        self.removeAsteroidBtn.clicked.connect(self.on_remove_asteroid_clicked)
        self.removeCometBtn.clicked.connect(self.on_remove_comet_clicked)
        self.removeSatelliteBtn.clicked.connect(self.on_remove_satellite_clicked)
        self.exit2Btn.clicked.connect(self.close)

    def open_add_asteroid(self):
        dialog = AddAsteroidDialog(self.model)
        dialog.exec()

    def on_add_comet_clicked(self):
        dialog = AddCometDialog(self.model)
        dialog.exec()

    def on_add_satellite_clicked(self):
        dialog = AddSatelliteDialog(self.model)
        dialog.exec()

    def on_remove_asteroid_clicked(self):
        print("Remove asteroid clicked")

    def on_remove_comet_clicked(self):
        print("Remove comet clicked")

    def on_remove_satellite_clicked(self):
        print("Remove satellite clicked")