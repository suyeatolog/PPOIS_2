from PySide6.QtWidgets import QDialog, QMessageBox, QTableWidgetItem, QHeaderView, QAbstractItemView
from PySide6.QtCore import Qt
from .search_window import Ui_SearchStudent
from storage.student_repository import StudentRepository
from src.interface.ui.table_mixin import StudentTableMixin

class SearchStudentDialog(QDialog, StudentTableMixin):
    def __init__(self):
        super().__init__()

        self.ui = Ui_SearchStudent()
        self.ui.setupUi(self)
        self.setWindowTitle("Поиск")

        self.ui.searchBtn.clicked.connect(self.on_search_clicked)
        self.ui.backBtn.clicked.connect(self.reject)

        self._repo = None
        self._found_students = []
        self._setup_result_table()

    def _setup_result_table(self):
        table = self.ui.searchResultTable

        table.setColumnCount(12)
        table.setRowCount(2)

        fio_item = QTableWidgetItem("ФИО студента")
        fio_item.setTextAlignment(Qt.AlignCenter)
        group_item = QTableWidgetItem("Группа")
        group_item.setTextAlignment(Qt.AlignCenter)
        social_item = QTableWidgetItem("Общественная работа (семестр)")
        social_item.setTextAlignment(Qt.AlignCenter)

        table.setItem(0, 0, fio_item)
        table.setItem(0, 1, group_item)
        table.setItem(0, 2, social_item)

        table.setSpan(0, 0, 2, 1)
        table.setSpan(0, 1, 2, 1)
        table.setSpan(0, 2, 1, 10)

        for i in range(10):
            sem_item = QTableWidgetItem(str(i + 1))
            sem_item.setTextAlignment(Qt.AlignCenter)
            table.setItem(1, 2 + i, sem_item)

        table.horizontalHeader().setVisible(False)
        table.verticalHeader().setVisible(False)

        header = table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        for col in range(1, table.columnCount()):
            header.setSectionResizeMode(col, QHeaderView.Stretch)

        table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        table.setSelectionMode(QAbstractItemView.NoSelection)
        table.setFocusPolicy(Qt.NoFocus)

        existing_style = table.styleSheet()
        table.setStyleSheet(
            existing_style
            + "\nQTableWidget { border-radius: 0px; }\n"
            + "QHeaderView { border-radius: 0px; }\n"
            + "QTableCornerButton::section { border-radius: 0px; border: 1px solid black; }\n"
            + "QTableWidget::item { border: 1px solid black; }\n"
        )


    def set_group_options(self, groups: list[str]):
        self.ui.groupBox.clear()
        self.ui.groupBox.addItems(groups)
        self.ui.groupBox.addItem("<Не выбрано>")

    def set_repo(self, repo: StudentRepository):
        self._repo = repo

    def on_search_clicked(self):
        if not self._repo:
            QMessageBox.critical(self, "Ошибка", "Репозиторий не установлен.")
            return

        last_name_input = self.ui.lastName.text().strip()

        selected_text_in_combo = self.ui.groupBox.currentText().strip()
        has_group_selection = selected_text_in_combo != "<Не выбрано>"
        group_input = selected_text_in_combo if has_group_selection else ""

        min_work = self.ui.socialWorkLowest.value()
        max_work = self.ui.socialWorkHighest.value()

        has_last_name = bool(last_name_input)
        has_group = bool(group_input and self.ui.groupBox.currentIndex() != -1)
        has_work_range = min_work > 0 or max_work > 0

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
            found_students = self._repo.find_students(**search_criteria)
            self._found_students = found_students

            if found_students:
                self._render_search_results(found_students)
                QMessageBox.information(self, "Успешно", f"Найдено записей ({len(found_students)}).")
            else:
                self._render_search_results([])
                QMessageBox.information(self, "Информация", "Студенты, соответствующие критериям, не найдены.")

        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Произошла ошибка при поиске: {e}")

    def _render_search_results(self, students):
        """Заполняет таблицу searchResultTable найденными студентами."""
        table = self.ui.searchResultTable
        table.setRowCount(2 + len(students))

        for row_idx, student in enumerate(students, start=2):
            values = student.to_table_row()
            for col_idx, text in enumerate(values):
                item = QTableWidgetItem(text)
                item.setTextAlignment(Qt.AlignCenter)
                table.setItem(row_idx, col_idx, item)

    def refresh(self, students):
        self.render_students(self.ui.searchTable, students)

