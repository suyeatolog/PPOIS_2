from PySide6.QtCore import Qt
from PySide6.QtWidgets import QAbstractItemView, QHeaderView, QTableWidgetItem, QMessageBox

class StudentTableMixin:

    def _init_pagination(self, pagination_size_combo, first_btn, prev_btn, current_label, next_btn, last_btn, table_widget=None):
        self._pagination_size_combo = pagination_size_combo
        self._first_page_btn = first_btn
        self._prev_arrow_btn = prev_btn
        self._current_page_label = current_label
        self._next_arrow_btn = next_btn
        self._last_page_btn = last_btn
        self._paginated_table = table_widget

        self._pagination_size_combo.currentTextChanged.connect(self._on_page_size_changed)
        self._first_page_btn.clicked.connect(lambda: self._go_to_page(1))
        self._prev_arrow_btn.clicked.connect(self._go_to_previous_page)
        self._next_arrow_btn.clicked.connect(self._go_to_next_page)
        self._last_page_btn.clicked.connect(self._go_to_last_page)

        self._all_data_for_pagination = []
        self._current_page = 1
        self._page_size = 5

        try:
            initial_size = int(self._pagination_size_combo.currentText())
            self._page_size = initial_size
        except ValueError:
            self._page_size = 5
            QMessageBox.warning(None, "Предупреждение", f"Некорректное значение размера страницы в combobox: {self._pagination_size_combo.currentText()}. Используется значение по умолчанию: {self._page_size}.")

    def _refresh_pagination(self, all_data):
        self._all_data_for_pagination = all_data
        self._current_page = 1

        try:
            self._page_size = int(self._pagination_size_combo.currentText())
        except ValueError:
            self._page_size = 5
            QMessageBox.warning(None, "Предупреждение", f"Некорректное значение размера страницы в combobox: {self._pagination_size_combo.currentText()}. Используется значение по умолчанию: {self._page_size}.")
        self._render_current_page()

    def _render_current_page(self):
        if not hasattr(self, '_all_data_for_pagination'):
            return
        
        table = self._paginated_table if self._paginated_table else self.ui.mainTable
        
        if not self._all_data_for_pagination:
            self.render_students(table, [])
            self._update_pagination_info()
            return
        
        start_index = (self._current_page - 1) * self._page_size
        end_index = start_index + self._page_size
        page_data = self._all_data_for_pagination[start_index:end_index]
        
        self.render_students(table, page_data)
        self._update_pagination_info()

    def _update_pagination_info(self):
        if not hasattr(self, '_all_data_for_pagination'):
            return

        total_items = len(self._all_data_for_pagination)
        total_pages = (total_items + self._page_size - 1) // self._page_size if total_items > 0 else 1

        self._current_page_label.setText(f"{self._current_page} / {total_pages}")
        self._last_page_btn.setText(str(total_pages))

        self._first_page_btn.setEnabled(self._current_page > 1)
        self._prev_arrow_btn.setEnabled(self._current_page > 1)
        self._next_arrow_btn.setEnabled(self._current_page < total_pages)
        self._last_page_btn.setEnabled(self._current_page < total_pages)

    def _on_page_size_changed(self, text):
        try:
            new_size = int(text)
            if new_size != self._page_size:
                self._page_size = new_size
                self._current_page = 1
                self._render_current_page()
        except ValueError:
            QMessageBox.warning(None, "Предупреждение", f"Некорректное значение размера страницы: {text}.")

    def _go_to_page(self, page_num):
        if not hasattr(self, '_all_data_for_pagination'):
            return

        total_items = len(self._all_data_for_pagination)
        total_pages = (total_items + self._page_size - 1) // self._page_size if total_items > 0 else 1

        if 1 <= page_num <= total_pages:
            self._current_page = page_num
            self._render_current_page()

    def _go_to_previous_page(self):
        if not hasattr(self, '_all_data_for_pagination'):
            return

        if self._current_page > 1:
            self._current_page -= 1
            self._render_current_page()

    def _go_to_next_page(self):
        if not hasattr(self, '_all_data_for_pagination'):
            return

        total_items = len(self._all_data_for_pagination)
        total_pages = (total_items + self._page_size - 1) // self._page_size if total_items > 0 else 1

        if self._current_page < total_pages:
            self._current_page += 1
            self._render_current_page()
    
    def _go_to_last_page(self):
        if not hasattr(self, '_all_data_for_pagination'):
            return

        total_items = len(self._all_data_for_pagination)
        total_pages = (total_items + self._page_size - 1) // self._page_size if total_items > 0 else 1
        if total_pages > 0:
            self._go_to_page(total_pages)

    def setup_student_table(self, table):
        column_count = 12
        table.setColumnCount(column_count)
        table.setRowCount(2)

        table.horizontalHeader().setVisible(False)
        table.verticalHeader().setVisible(False)

        fio_item = self._make_center_item("ФИО студента")
        group_item = self._make_center_item("Группа")
        social_item = self._make_center_item("Общественная работа (семестр)")

        table.setItem(0, 0, fio_item)
        table.setItem(0, 1, group_item)
        table.setItem(0, 2, social_item)

        table.setSpan(0, 0, 2, 1)
        table.setSpan(0, 1, 2, 1)
        table.setSpan(0, 2, 1, 10)

        for i in range(10):
            sem_item = self._make_center_item(str(i + 1))
            table.setItem(1, 2 + i, sem_item)

        header = table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        for col in range(1, column_count):
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

    def render_students(self, table, students):
        table.setRowCount(2 + len(students))
        for row_idx, student in enumerate(students, start=2):
            values = student.to_table_row()
            for col_idx, text in enumerate(values):
                item = self._make_center_item(text)
                table.setItem(row_idx, col_idx, item)

    @staticmethod
    def _make_center_item(text):
        item = QTableWidgetItem(text)
        item.setTextAlignment(Qt.AlignCenter)
        return item