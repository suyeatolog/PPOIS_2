from PySide6.QtWidgets import QDialog, QMessageBox
from .search_window import Ui_SearchStudent
from storage.student_repository import StudentRepository

class SearchStudentDialog(QDialog):
    def __init__(self):
        super.__init__()

        self.ui = Ui_SearchStudent()
        self.ui.setupUi(self)
        self.setWindowTitle("Поиск")

        self.ui.deleteBtn.clicked.connect(self.on_search_clicked)
        self.ui.backBtn.clicked.connect(self.reject)

        self._repo = None


    def set_group_options(self, groups: list[str]):
        self.ui.groupBox.clear()
        self.ui.groupBox.addItems(groups)

    def on_search_clicked(self, repo: StudentRepository):
        if not self._repo:
            QMessageBox.critical(self, "Ошибка", "Репозиторий не установлен.")
            return
    
        last_name_input = self.ui.lastName.text().strip()
        group_input = self.ui.groupBox.currentText().strip()
        min_work = self.ui.socialWorkLowest.value()
        max_work = self.ui.socialWorkHighest.value()

        has_last_name = bool(last_name_input)
        has_group = bool(group_input and self.ui.groupBox.currentIndex() != -1)
        has_work_range = min_work > 0 or max_work != 0

        valid_combinations = [
            (has_last_name and not has_group and not has_work_range),
            (not has_last_name and has_group and not has_work_range),
            (has_last_name and not has_group and has_work_range),
            (not has_last_name and has_group and has_work_range),
        ]

        if not any(valid_combinations):
            QMessageBox.warning(
                self,
                "Ошибка ввода",
                "Пожалуйста, выберите один из следующих вариантов:\n"
                "- Только фамилия студента\n"
                "- Только номер группы\n"
                "- Фамилия студента и диапазон общественной работы\n"
                "- Номер группы и диапазон общественной работы",
            )
            return
        
        if min_work > max_work:
            QMessageBox.warning(
                self,
                "Ошибка ввода",
                "Минимальное значение работы не может быть больше максимального.",
            )
            return
        
        search_criteria = {}
        if has_last_name:
            search_criteria['last_name'] = last_name_input
        if has_group:
            search_criteria['group'] = group_input
        if has_work_range:
            search_criteria['min_total_work'] = min_work
            search_criteria['max_total_work'] = max_work

        print(f"DEBUG: Search criteria: {search_criteria}")

        try:
            found_count = self._repo.find_students(**search_criteria)
            if found_count > 0:
                QMessageBox.information(self, "Успешно", f"Найдено записей ({found_count}).")
                self.accept()
            else:
                QMessageBox.information(self, "Информация", "Студенты, соответствующие критериям, не найдены.")
                self.accept()
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Произошла ошибка при поиске: {e}")
