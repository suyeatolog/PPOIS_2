import sys
from pathlib import Path

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QAbstractItemView,
    QFileDialog,
    QHeaderView,
    QMainWindow,
    QTableWidgetItem,
    QVBoxLayout,
    QSizePolicy,
    QLabel,
    QDialog
)

from PySide6.QtGui import QPixmap
from interface.ui.main_window import Ui_MainWindow
from interface.ui.add_student_dialog import AddStudentDialog
from interface.ui.delete_student_dialog import DeleteStudentDialog

from persistence.xml_students_sax import read_students_from_xml
from storage.student_repository import StudentRepository


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Главная таблица")
        self.setMinimumHeight(self.minimumHeight() + 80)
        self.setMinimumWidth(self.minimumWidth() + 80)

        self.ui.introOrTableWidget.setCurrentIndex(0)
        self.ui.buttonsWidget.setCurrentIndex(0)

        self.ui.introOrTableWidget.tabBar().hide()
        self.ui.buttonsWidget.tabBar().hide()

        self._setup_main_table()
        self._setup_intro_image()

        self.ui.loadButton.clicked.connect(self.load_data)
        self.ui.exitButton.clicked.connect(self.close)
        self.ui.addButton.clicked.connect(self.add_student)
        self.ui.deleteButton.clicked.connect(self.delete_student)

        self._repo = StudentRepository()

    def _setup_intro_image(self) -> None:
        tab_page = self.ui.introOrTableWidget.widget(0)

        if not tab_page:
            return

        self.intro_image_label = QLabel()

        image_path = "images/bg.jpeg"
        pixmap = QPixmap(image_path)

        if pixmap.isNull():
            self.intro_image_label.setText("Изображение не найдено:\n" + image_path)
            self.intro_image_label.setAlignment(Qt.AlignCenter)
        else:
            self.intro_image_label.setPixmap(pixmap)
            self.intro_image_label.setScaledContents(False)

        self.intro_image_label.setSizePolicy(
            QSizePolicy.Expanding, QSizePolicy.Expanding
        )
        self.intro_image_label.setAlignment(Qt.AlignCenter)

        if tab_page.layout() is not None:
            tab_page.layout().addWidget(self.intro_image_label)
        else:
            layout = QVBoxLayout(tab_page)
            layout.addWidget(self.intro_image_label)

    def _render_students(self) -> None:
        table = self.ui.mainTable
        students = self._repo.all()

        table.setRowCount(2 + len(students))

        for row_idx, student in enumerate(students, start=2):
            values = student.to_table_row()
            for col_idx, text in enumerate(values):
                item = QTableWidgetItem(text)
                item.setTextAlignment(Qt.AlignCenter)
                table.setItem(row_idx, col_idx, item)

    def _setup_main_table(self) -> None:
        table = self.ui.mainTable

        column_count = 12
        table.setColumnCount(column_count)

        table.setRowCount(2)

        table.horizontalHeader().setVisible(False)
        table.verticalHeader().setVisible(False)

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

    def load_data(self) -> None:
        students_dir = str(Path(__file__).resolve().parents[1] / "students")
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Загрузить студентов",
            students_dir,
            "XML files (*.xml)",
        )
        if not file_path:
            return

        students = read_students_from_xml(file_path)
        self._repo.replace_all(students)
        self._render_students()

        self.ui.introOrTableWidget.setCurrentIndex(1)
        self.ui.buttonsWidget.setCurrentIndex(1)

    def add_student(self) -> None:
        dialog = AddStudentDialog()      
        result = dialog.exec()

        if result == QDialog.DialogCode.Accepted:
            created_student = dialog.get_created_student()

            if created_student:
                self._repo.add(created_student)
                self._render_students()
                print(f"Студент добавлен: {created_student.full_name}")
            else:
                print("Диалог завершился успешно, но студент не был создан.")
    
    def delete_student(self) -> None:
        dialog = DeleteStudentDialog()

        unique_groups = self._repo.get_unique_groups()
        dialog.set_group_options(unique_groups)
        dialog.set_repo(self._repo)

        result = dialog.exec()
        if result == QDialog.DialogCode.Accepted:
            self._render_students()
            print("Студенты удалены, таблица обновлена.")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())