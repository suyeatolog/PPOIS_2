from PySide6.QtWidgets import QDialog
from ..uistransformed.showbodies import Ui_Dialog

class ShowBodiesDialog(QDialog, Ui_Dialog):
    def __init__(self, model):
        super().__init__()
        self.setupUi(self)
        self.model = model

        self.populate_list()

        self.exit1Btn.clicked.connect(self.close)

    def populate_list(self):
        bodies = self.model.get_all_bodies()
        for body in bodies:
            info = body.get_info()
            self.listBodiesWidget.addItem(info)