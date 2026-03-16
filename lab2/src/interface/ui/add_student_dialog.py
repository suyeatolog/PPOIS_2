from PySide6.QtWidgets import QDialog
from .add_window import Ui_AddStudent


class AddStudentDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_AddStudent()
        self.ui.setupUi(self)