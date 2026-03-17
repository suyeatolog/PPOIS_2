from PySide6.QtWidgets import QDialog, QMessageBox
from .add_window import Ui_AddStudent
from domain.student import Student


class AddStudentDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_AddStudent()
        self.ui.setupUi(self)

        self.ui.addBtn.clicked.connect(self.on_add_clicked)
        self.ui.backBtn.clicked.connect(self.reject)

        self.created_student = None

    def on_add_clicked(self):
        last_name = self.ui.lastName.text().strip()
        first_name = self.ui.firstName.text().strip()
        middle_name = self.ui.middleName.text().strip()
        group = self.ui.group.text().strip()

        if not last_name or not first_name or not middle_name or not group:
            QMessageBox.warning(self, "Ошибка ввода", "Фамилия, имя, отчество и группа должны быть заполнены.")
            return
        
        sem_values = [
            self.ui.semBox1.value(),
            self.ui.semBox2.value(),
            self.ui.semBox3.value(),
            self.ui.semBox4.value(),
            self.ui.semBox5.value(),
            self.ui.semBox6.value(),
            self.ui.semBox7.value(),
            self.ui.semBox8.value(),
            self.ui.semBox9.value(),
            self.ui.semBox10.value(),
        ]

        try:
            new_student = Student(
                last_name=last_name,
                first_name=first_name,
                middle_name=middle_name,
                group=group,
                social_work_by_semester=sem_values
            )

            self.created_student = new_student
            self.accept()

        except Exception as e:
             QMessageBox.critical(self, "Ошибка", f"Не удалось создать студента: {e}")

    def get_created_student(self):
        return self.created_student
