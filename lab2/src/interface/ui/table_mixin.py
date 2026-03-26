from PySide6.QtCore import Qt
from PySide6.QtWidgets import QAbstractItemView, QHeaderView, QTableWidgetItem

class StudentTableMixin:
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