from PySide6.QtWidgets import QDialog, QMessageBox
from .search_window import Ui_SearchStudent
from storage.student_repository import StudentRepository
from .table_mixin import StudentTableMixin

class SearchStudentDialog(QDialog, StudentTableMixin):
    def __init__(self):
        super().__init__()

        self.ui = Ui_SearchStudent()
        self.ui.setupUi(self)
        self.setWindowTitle("Поиск")

        self.ui.searchBtn.clicked.connect(self.on_search_clicked)
        self.ui.backBtn.clicked.connect(self.reject)

        self._init_pagination(
            pagination_size_combo=self.ui.paginationSize,
            first_btn=self.ui.firstPageBtn,
            prev_btn=self.ui.previousArrowBtn,
            current_label=self.ui.currentPageLabel,
            next_btn=self.ui.nextArrowBtn,
            last_btn=self.ui.lastPageBtn,
            table_widget=self.ui.searchResultTable
        )

        self._repo = None
        self._found_students = []
        self._setup_result_table()

    def _setup_result_table(self):
        self.setup_student_table(self.ui.searchResultTable)


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
        """Заполняет таблицу searchResultTable найденными студентами с пагинацией."""
        self._refresh_pagination(students)