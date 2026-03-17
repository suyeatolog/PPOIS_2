from PySide6.QtWidgets import QDialog, QMessageBox
from .delete_window import Ui_deleteStudent
from domain.student import Student

class DeleteStudentDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_deleteStudent()
        self.ui.setupUi(self)

        self.ui.deleteBtn.clicked.connect(self.on_delete_clicked)
        self.ui.backBtn.clicked.connect(self.reject)

        self._student_to_delete = None

    def set_group_options(self, groups: list[str]):
        self.ui.groupBox.clear()
        self.ui.groupBox.addItems(groups)

    def on_delete_clicked(self):
        pass