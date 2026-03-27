import sys
from pathlib import Path

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QFileDialog,
    QMainWindow,
    QVBoxLayout,
    QSizePolicy,
    QLabel,
    QDialog
)

from PySide6.QtGui import QPixmap
from interface.ui.main_window import Ui_MainWindow
from interface.ui.add_student_dialog import AddStudentDialog
from interface.ui.delete_student_dialog import DeleteStudentDialog
from interface.ui.search_student_dialog import SearchStudentDialog

from persistence.xml_students_sax import read_students_from_xml
from storage.student_repository import StudentRepository
from interface.ui.table_mixin import StudentTableMixin


class MainWindow(QMainWindow, StudentTableMixin):
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

        self._init_pagination(
            pagination_size_combo=self.ui.paginationSize,
            first_btn=self.ui.firstPageBtn,
            prev_btn=self.ui.previousArrowBtn,
            current_label=self.ui.currentPageLabel,
            next_btn=self.ui.nextArrowBtn,
            last_btn=self.ui.lastPageBtn,
            table_widget=self.ui.mainTable
        )

        self.ui.loadButton.clicked.connect(self.load_data)
        self.ui.exitButton.clicked.connect(self.close)
        self.ui.addButton.clicked.connect(self.add_student)
        self.ui.deleteButton.clicked.connect(self.delete_student)
        self.ui.searchButton.clicked.connect(self.search_student)

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

    def _setup_main_table(self) -> None:
        self.setup_student_table(self.ui.mainTable)

    def _render_students(self) -> None:
        all_students = self._repo.all()
        self._refresh_pagination(all_students)

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

    def search_student(self) -> None:
        dialog = SearchStudentDialog()

        unique_groups = self._repo.get_unique_groups()
        dialog.set_group_options(unique_groups)
        dialog.set_repo(self._repo)

        dialog.exec()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())