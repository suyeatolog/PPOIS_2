# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'deleteWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QSpinBox, QVBoxLayout,
    QWidget)

class Ui_DeleteStudent(object):
    def setupUi(self, deleteStudent):
        if not deleteStudent.objectName():
            deleteStudent.setObjectName(u"deleteStudent")
        deleteStudent.resize(396, 380)
        deleteStudent.setMinimumSize(QSize(396, 380))
        deleteStudent.setMaximumSize(QSize(396, 380))
        deleteStudent.setStyleSheet(u"background-color: rgb(214, 214, 216);")
        self.verticalLayout_2 = QVBoxLayout(deleteStudent)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(deleteStudent)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QFrame {\n"
"    background-color: rgba(255, 255, 255, 30); \n"
"    border-radius: 10px;\n"
"    border: 1px solid rgba(255, 255, 255, 50);\n"
"}\n"
"\n"
"QTableWidget {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    gridline-color: rgba(255, 255, 255, 20);\n"
"}\n"
"")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.deleteLabel = QLabel(self.frame)
        self.deleteLabel.setObjectName(u"deleteLabel")
        self.deleteLabel.setMaximumSize(QSize(16777215, 50))
        self.deleteLabel.setStyleSheet(u"QLabel {\n"
"	background-color: rgb(172, 172, 172);\n"
"	color: white;\n"
"	padding: 5px 10px;\n"
"	border-radius: 6px;\n"
"	font-weight: bold;\n"
"	font-size: 14px;\n"
"	qproperty-alignment: 'AlignCenter';\n"
"	border: none;\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.deleteLabel)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"QFrame {\n"
"    background-color: rgba(255, 255, 255, 30); \n"
"    border-radius: 10px;\n"
"    border: 1px solid rgba(255, 255, 255, 50);\n"
"}\n"
"\n"
"QTableWidget {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    gridline-color: rgba(255, 255, 255, 20);\n"
"}\n"
"")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lastName = QLineEdit(self.frame_2)
        self.lastName.setObjectName(u"lastName")
        self.lastName.setMinimumSize(QSize(100, 50))
        self.lastName.setStyleSheet(u"QLineEdit {\n"
"    background-color: #f4f4f4;\n"
"    border: 2px solid #bdc3c7;\n"
"    border-radius: 6px;\n"
"    color: #2c3e50;\n"
"    selection-background-color: #3498db;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #3498db;\n"
"    background-color: #ffffff;\n"
"}\n"
"\n"
"QLineEdit::placeholder {\n"
"    color: #95a5a6;\n"
"    font-style: italic;\n"
"}\n"
"")

        self.horizontalLayout_2.addWidget(self.lastName)

        self.groupBox = QComboBox(self.frame_2)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(0, 50))
        self.groupBox.setStyleSheet(u"QComboBox {\n"
"    background-color: #f4f4f4;\n"
"    border: 2px solid #bdc3c7;\n"
"    border-radius: 6px;\n"
"    color: #2c3e50;\n"
"    selection-background-color: #3498db;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QComboBox:focus {\n"
"    border: 2px solid #3498db;\n"
"    background-color: #ffffff;\n"
"}")

        self.horizontalLayout_2.addWidget(self.groupBox)


        self.verticalLayout.addWidget(self.frame_2)

        self.socialWorkLabel = QLabel(self.frame)
        self.socialWorkLabel.setObjectName(u"socialWorkLabel")
        self.socialWorkLabel.setMaximumSize(QSize(16777215, 50))
        self.socialWorkLabel.setStyleSheet(u"QLabel {\n"
"	background-color: rgb(172, 172, 172);\n"
"	color: white;\n"
"	padding: 5px 10px;\n"
"	border-radius: 6px;\n"
"	font-weight: bold;\n"
"	font-size: 14px;\n"
"	qproperty-alignment: 'AlignCenter';\n"
"	border: none;\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.socialWorkLabel)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"QFrame {\n"
"    background-color: rgba(255, 255, 255, 30); \n"
"    border-radius: 10px;\n"
"    border: 1px solid rgba(255, 255, 255, 50);\n"
"}\n"
"\n"
"QTableWidget {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    gridline-color: rgba(255, 255, 255, 20);\n"
"}\n"
"")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.socialWorkLowest = QSpinBox(self.frame_4)
        self.socialWorkLowest.setObjectName(u"socialWorkLowest")
        self.socialWorkLowest.setMinimumSize(QSize(0, 25))
        self.socialWorkLowest.setStyleSheet(u"QSpinBox {\n"
"    background-color: #f4f4f4;\n"
"    border: 2px solid #bdc3c7;\n"
"    border-radius: 6px;\n"
"    color: #2c3e50;\n"
"    font-size: 14px;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"	qproperty-alignment: 'AlignCenter';\n"
"}\n"
"\n"
"QSpinBox:focus {\n"
"    border: 2px solid #3498db;\n"
"    background-color: #ffffff;\n"
"}\n"
"\n"
"QSpinBox::up-button, QSpinBox::down-button {\n"
"    width: 0px;\n"
"    height: 0px;\n"
"    border: none;\n"
"    background: transparent;\n"
"}\n"
"")

        self.horizontalLayout_3.addWidget(self.socialWorkLowest)

        self.socialWorkHighest = QSpinBox(self.frame_4)
        self.socialWorkHighest.setObjectName(u"socialWorkHighest")
        self.socialWorkHighest.setMinimumSize(QSize(0, 25))
        self.socialWorkHighest.setStyleSheet(u"QSpinBox {\n"
"    background-color: #f4f4f4;\n"
"    border: 2px solid #bdc3c7;\n"
"    border-radius: 6px;\n"
"    color: #2c3e50;\n"
"    font-size: 14px;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"	qproperty-alignment: 'AlignCenter';\n"
"}\n"
"\n"
"QSpinBox:focus {\n"
"    border: 2px solid #3498db;\n"
"    background-color: #ffffff;\n"
"}\n"
"\n"
"QSpinBox::up-button, QSpinBox::down-button {\n"
"    width: 0px;\n"
"    height: 0px;\n"
"    border: none;\n"
"    background: transparent;\n"
"}\n"
"")

        self.horizontalLayout_3.addWidget(self.socialWorkHighest)


        self.verticalLayout.addWidget(self.frame_4)


        self.verticalLayout_2.addWidget(self.frame)

        self.frame_3 = QFrame(deleteStudent)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"QFrame {\n"
"    background-color: rgba(255, 255, 255, 30); \n"
"    border-radius: 10px;\n"
"    border: 1px solid rgba(255, 255, 255, 50);\n"
"}\n"
"\n"
"QTableWidget {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    gridline-color: rgba(255, 255, 255, 20);\n"
"}\n"
"")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.backBtn = QPushButton(self.frame_3)
        self.backBtn.setObjectName(u"backBtn")
        self.backBtn.setStyleSheet(u"QPushButton {	\n"
"	background-color: rgb(85, 87, 87);\n"
"	border-style: solid;\n"
"	border-width: 2px;\n"
"	border-color: #26282a;\n"
"	border-radius: 10px;\n"
"	padding: 5px;\n"
"	font: bold 14px \"Arial\", sans-serif;\n"
"	color: #ffffff;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(164, 167, 167);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(85, 87, 87);\n"
"	border-style: inset;\n"
"}")

        self.horizontalLayout.addWidget(self.backBtn)

        self.deleteBtn = QPushButton(self.frame_3)
        self.deleteBtn.setObjectName(u"deleteBtn")
        self.deleteBtn.setStyleSheet(u"QPushButton {	\n"
"	background-color: rgb(119, 0, 33);\n"
"	border-style: solid;\n"
"	border-width: 2px;\n"
"	border-color: #26282a;\n"
"	border-radius: 10px;\n"
"	padding: 5px;\n"
"	font: bold 14px \"Arial\", sans-serif;\n"
"	color: #ffffff;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(203, 0, 29);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(119, 0, 33);\n"
"	border-style: inset;\n"
"}")

        self.horizontalLayout.addWidget(self.deleteBtn)


        self.verticalLayout_2.addWidget(self.frame_3)


        self.retranslateUi(deleteStudent)

        QMetaObject.connectSlotsByName(deleteStudent)
    # setupUi

    def retranslateUi(self, deleteStudent):
        deleteStudent.setWindowTitle(QCoreApplication.translate("deleteStudent", u"Dialog", None))
        self.deleteLabel.setText(QCoreApplication.translate("deleteStudent", u"\u0423\u0434\u0430\u043b\u0435\u043d\u0438\u0435 \u0441\u0442\u0443\u0434\u0435\u043d\u0442\u0430", None))
        self.lastName.setText("")
        self.lastName.setPlaceholderText(QCoreApplication.translate("deleteStudent", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0444\u0430\u043c\u0438\u043b\u0438\u044e...", None))
        self.groupBox.setPlaceholderText(QCoreApplication.translate("deleteStudent", u"\u0413\u0440\u0443\u043f\u043f\u0430...", None))
        self.socialWorkLabel.setText(QCoreApplication.translate("deleteStudent", u"\u041e\u0431\u0449\u0435\u0441\u0442\u0432\u0435\u043d\u043d\u0430\u044f \u0440\u0430\u0431\u043e\u0442\u0430", None))
        self.backBtn.setText(QCoreApplication.translate("deleteStudent", u"\u041d\u0430\u0437\u0430\u0434", None))
        self.deleteBtn.setText(QCoreApplication.translate("deleteStudent", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0441\u0442\u0443\u0434\u0435\u043d\u0442\u0430", None))
    # retranslateUi

