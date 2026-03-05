# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'addWindow.ui'
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

class Ui_AddStudent(object):
    def setupUi(self, AddStudent):
        if not AddStudent.objectName():
            AddStudent.setObjectName(u"AddStudent")
        AddStudent.resize(375, 801)
        AddStudent.setMinimumSize(QSize(375, 801))
        AddStudent.setMaximumSize(QSize(375, 801))
        AddStudent.setStyleSheet(u"background-color: rgb(122, 122, 122);")
        self.verticalLayout_5 = QVBoxLayout(AddStudent)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_2 = QFrame(AddStudent)
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
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.addLabel = QLabel(self.frame_2)
        self.addLabel.setObjectName(u"addLabel")
        self.addLabel.setMaximumSize(QSize(16777215, 50))
        self.addLabel.setStyleSheet(u"QLabel {\n"
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

        self.verticalLayout_4.addWidget(self.addLabel)

        self.verticalSpacer = QSpacerItem(20, 15, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
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

        self.verticalLayout_3.addWidget(self.lastName)

        self.firstName = QLineEdit(self.frame_2)
        self.firstName.setObjectName(u"firstName")
        self.firstName.setMinimumSize(QSize(100, 50))
        self.firstName.setStyleSheet(u"QLineEdit {\n"
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

        self.verticalLayout_3.addWidget(self.firstName)

        self.middleName = QLineEdit(self.frame_2)
        self.middleName.setObjectName(u"middleName")
        self.middleName.setMinimumSize(QSize(100, 50))
        self.middleName.setStyleSheet(u"QLineEdit {\n"
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

        self.verticalLayout_3.addWidget(self.middleName)

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
"    qproperty-alignment: 'AlignCenter';\n"
"}\n"
"\n"
"QComboBox:focus {\n"
"    border: 2px solid #3498db;\n"
"    background-color: #ffffff;\n"
"}")

        self.verticalLayout_3.addWidget(self.groupBox)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)


        self.verticalLayout_5.addWidget(self.frame_2)

        self.frame = QFrame(AddStudent)
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
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.semLabel1 = QLabel(self.frame)
        self.semLabel1.setObjectName(u"semLabel1")
        self.semLabel1.setMinimumSize(QSize(200, 25))
        self.semLabel1.setMaximumSize(QSize(16777215, 50))
        self.semLabel1.setStyleSheet(u"QLabel {\n"
"	background-color: rgb(172, 172, 172);\n"
"	color: white;\n"
"	padding: 5px 10px;\n"
"	border-radius: 5px;\n"
"	font-weight: bold;\n"
"	font-size: 14px;\n"
"	qproperty-alignment: 'AlignCenter';\n"
"	border: none;\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.semLabel1)

        self.semLabel2 = QLabel(self.frame)
        self.semLabel2.setObjectName(u"semLabel2")
        self.semLabel2.setMinimumSize(QSize(100, 25))
        self.semLabel2.setMaximumSize(QSize(16777215, 50))
        self.semLabel2.setStyleSheet(u"QLabel {\n"
"	background-color: rgb(172, 172, 172);\n"
"	color: white;\n"
"	padding: 5px 10px;\n"
"	border-radius: 5px;\n"
"	font-weight: bold;\n"
"	font-size: 14px;\n"
"	qproperty-alignment: 'AlignCenter';\n"
"	border: none;\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.semLabel2)

        self.semLabel3 = QLabel(self.frame)
        self.semLabel3.setObjectName(u"semLabel3")
        self.semLabel3.setMinimumSize(QSize(100, 25))
        self.semLabel3.setMaximumSize(QSize(16777215, 50))
        self.semLabel3.setStyleSheet(u"QLabel {\n"
"	background-color: rgb(172, 172, 172);\n"
"	color: white;\n"
"	padding: 5px 10px;\n"
"	border-radius: 5px;\n"
"	font-weight: bold;\n"
"	font-size: 14px;\n"
"	qproperty-alignment: 'AlignCenter';\n"
"	border: none;\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.semLabel3)

        self.semLabel4 = QLabel(self.frame)
        self.semLabel4.setObjectName(u"semLabel4")
        self.semLabel4.setMinimumSize(QSize(100, 0))
        self.semLabel4.setMaximumSize(QSize(16777215, 50))
        self.semLabel4.setStyleSheet(u"QLabel {\n"
"	background-color: rgb(172, 172, 172);\n"
"	color: white;\n"
"	padding: 5px 10px;\n"
"	border-radius: 5px;\n"
"	font-weight: bold;\n"
"	font-size: 14px;\n"
"	qproperty-alignment: 'AlignCenter';\n"
"	border: none;\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.semLabel4)

        self.semLabel5 = QLabel(self.frame)
        self.semLabel5.setObjectName(u"semLabel5")
        self.semLabel5.setMinimumSize(QSize(100, 0))
        self.semLabel5.setMaximumSize(QSize(16777215, 50))
        self.semLabel5.setStyleSheet(u"QLabel {\n"
"	background-color: rgb(172, 172, 172);\n"
"	color: white;\n"
"	padding: 5px 10px;\n"
"	border-radius: 5px;\n"
"	font-weight: bold;\n"
"	font-size: 14px;\n"
"	qproperty-alignment: 'AlignCenter';\n"
"	border: none;\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.semLabel5)

        self.semLabel6 = QLabel(self.frame)
        self.semLabel6.setObjectName(u"semLabel6")
        self.semLabel6.setMinimumSize(QSize(100, 0))
        self.semLabel6.setMaximumSize(QSize(16777215, 50))
        self.semLabel6.setStyleSheet(u"QLabel {\n"
"	background-color: rgb(172, 172, 172);\n"
"	color: white;\n"
"	padding: 5px 10px;\n"
"	border-radius: 5px;\n"
"	font-weight: bold;\n"
"	font-size: 14px;\n"
"	qproperty-alignment: 'AlignCenter';\n"
"	border: none;\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.semLabel6)

        self.semLabel7 = QLabel(self.frame)
        self.semLabel7.setObjectName(u"semLabel7")
        self.semLabel7.setMinimumSize(QSize(100, 0))
        self.semLabel7.setMaximumSize(QSize(16777215, 50))
        self.semLabel7.setStyleSheet(u"QLabel {\n"
"	background-color: rgb(172, 172, 172);\n"
"	color: white;\n"
"	padding: 5px 10px;\n"
"	border-radius: 5px;\n"
"	font-weight: bold;\n"
"	font-size: 14px;\n"
"	qproperty-alignment: 'AlignCenter';\n"
"	border: none;\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.semLabel7)

        self.semLabel8 = QLabel(self.frame)
        self.semLabel8.setObjectName(u"semLabel8")
        self.semLabel8.setMinimumSize(QSize(100, 0))
        self.semLabel8.setMaximumSize(QSize(16777215, 50))
        self.semLabel8.setStyleSheet(u"QLabel {\n"
"	background-color: rgb(172, 172, 172);\n"
"	color: white;\n"
"	padding: 5px 10px;\n"
"	border-radius: 5px;\n"
"	font-weight: bold;\n"
"	font-size: 14px;\n"
"	qproperty-alignment: 'AlignCenter';\n"
"	border: none;\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.semLabel8)

        self.semLabel9 = QLabel(self.frame)
        self.semLabel9.setObjectName(u"semLabel9")
        self.semLabel9.setMinimumSize(QSize(150, 0))
        self.semLabel9.setMaximumSize(QSize(16777215, 50))
        self.semLabel9.setStyleSheet(u"QLabel {\n"
"	background-color: rgb(172, 172, 172);\n"
"	color: white;\n"
"	padding: 5px 10px;\n"
"	border-radius: 5px;\n"
"	font-weight: bold;\n"
"	font-size: 14px;\n"
"	qproperty-alignment: 'AlignCenter';\n"
"	border: none;\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.semLabel9)

        self.semLabel10 = QLabel(self.frame)
        self.semLabel10.setObjectName(u"semLabel10")
        self.semLabel10.setMinimumSize(QSize(100, 0))
        self.semLabel10.setMaximumSize(QSize(16777215, 50))
        self.semLabel10.setStyleSheet(u"QLabel {\n"
"	background-color: rgb(172, 172, 172);\n"
"	color: white;\n"
"	padding: 5px 10px;\n"
"	border-radius: 5px;\n"
"	font-weight: bold;\n"
"	font-size: 14px;\n"
"	qproperty-alignment: 'AlignCenter';\n"
"	border: none;\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.semLabel10)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.semBox1 = QSpinBox(self.frame)
        self.semBox1.setObjectName(u"semBox1")
        self.semBox1.setMinimumSize(QSize(0, 25))
        self.semBox1.setStyleSheet(u"QSpinBox {\n"
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

        self.verticalLayout_2.addWidget(self.semBox1)

        self.semBox2 = QSpinBox(self.frame)
        self.semBox2.setObjectName(u"semBox2")
        self.semBox2.setMinimumSize(QSize(0, 25))
        self.semBox2.setStyleSheet(u"QSpinBox {\n"
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

        self.verticalLayout_2.addWidget(self.semBox2)

        self.semBox3 = QSpinBox(self.frame)
        self.semBox3.setObjectName(u"semBox3")
        self.semBox3.setMinimumSize(QSize(0, 25))
        self.semBox3.setStyleSheet(u"QSpinBox {\n"
"    background-color: #f4f4f4;\n"
"    border: 2px solid #bdc3c7;\n"
"    border-radius: 6px;\n"
"    color: #2c3e50;\n"
"    font-size: 14px;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    qproperty-alignment: 'AlignCenter';\n"
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

        self.verticalLayout_2.addWidget(self.semBox3)

        self.semBox4 = QSpinBox(self.frame)
        self.semBox4.setObjectName(u"semBox4")
        self.semBox4.setMinimumSize(QSize(0, 25))
        self.semBox4.setStyleSheet(u"QSpinBox {\n"
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

        self.verticalLayout_2.addWidget(self.semBox4)

        self.semBox5 = QSpinBox(self.frame)
        self.semBox5.setObjectName(u"semBox5")
        self.semBox5.setMinimumSize(QSize(0, 25))
        self.semBox5.setStyleSheet(u"QSpinBox {\n"
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

        self.verticalLayout_2.addWidget(self.semBox5)

        self.semBox6 = QSpinBox(self.frame)
        self.semBox6.setObjectName(u"semBox6")
        self.semBox6.setMinimumSize(QSize(0, 25))
        self.semBox6.setStyleSheet(u"QSpinBox {\n"
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

        self.verticalLayout_2.addWidget(self.semBox6)

        self.semBox7 = QSpinBox(self.frame)
        self.semBox7.setObjectName(u"semBox7")
        self.semBox7.setMinimumSize(QSize(0, 25))
        self.semBox7.setStyleSheet(u"QSpinBox {\n"
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

        self.verticalLayout_2.addWidget(self.semBox7)

        self.semBox8 = QSpinBox(self.frame)
        self.semBox8.setObjectName(u"semBox8")
        self.semBox8.setMinimumSize(QSize(0, 25))
        self.semBox8.setStyleSheet(u"QSpinBox {\n"
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

        self.verticalLayout_2.addWidget(self.semBox8)

        self.semBox9 = QSpinBox(self.frame)
        self.semBox9.setObjectName(u"semBox9")
        self.semBox9.setMinimumSize(QSize(0, 25))
        self.semBox9.setStyleSheet(u"QSpinBox {\n"
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

        self.verticalLayout_2.addWidget(self.semBox9)

        self.semBox10 = QSpinBox(self.frame)
        self.semBox10.setObjectName(u"semBox10")
        self.semBox10.setMinimumSize(QSize(0, 25))
        self.semBox10.setStyleSheet(u"QSpinBox {\n"
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

        self.verticalLayout_2.addWidget(self.semBox10)


        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.verticalLayout_5.addWidget(self.frame)

        self.frame_3 = QFrame(AddStudent)
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
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.backBtn = QPushButton(self.frame_3)
        self.backBtn.setObjectName(u"backBtn")
        self.backBtn.setStyleSheet(u"QPushButton {	\n"
"	background-color: rgb(85, 87, 87);\n"
"	border-style: solid;\n"
"	border-width: 2px;\n"
"	border-color: #26282a;\n"
"	border-radius: 10px;\n"
"	padding: 5px;\n"
"	font: bold 14px \"Segoe UI\", sans-serif;\n"
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

        self.horizontalLayout_2.addWidget(self.backBtn)

        self.addBtn = QPushButton(self.frame_3)
        self.addBtn.setObjectName(u"addBtn")
        self.addBtn.setStyleSheet(u"QPushButton {	\n"
"	background-color: rgb(2, 104, 75);\n"
"	border-style: solid;\n"
"	border-width: 2px;\n"
"	border-color: #26282a;\n"
"	border-radius: 10px;\n"
"	padding: 5px;\n"
"	font: bold 14px \"Segoe UI\", sans-serif;\n"
"	color: #ffffff;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(1, 186, 102);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(2, 104, 75);\n"
"	border-style: inset;\n"
"}")

        self.horizontalLayout_2.addWidget(self.addBtn)


        self.verticalLayout_5.addWidget(self.frame_3)


        self.retranslateUi(AddStudent)

        QMetaObject.connectSlotsByName(AddStudent)
    # setupUi

    def retranslateUi(self, AddStudent):
        AddStudent.setWindowTitle(QCoreApplication.translate("AddStudent", u"Dialog", None))
        self.addLabel.setText(QCoreApplication.translate("AddStudent", u"\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u0441\u0442\u0443\u0434\u0435\u043d\u0442\u0430", None))
        self.lastName.setText("")
        self.lastName.setPlaceholderText(QCoreApplication.translate("AddStudent", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0444\u0430\u043c\u0438\u043b\u0438\u044e...", None))
        self.firstName.setText("")
        self.firstName.setPlaceholderText(QCoreApplication.translate("AddStudent", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0438\u043c\u044f...", None))
        self.middleName.setText("")
        self.middleName.setPlaceholderText(QCoreApplication.translate("AddStudent", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043e\u0442\u0447\u0435\u0441\u0442\u0432\u043e...", None))
        self.groupBox.setPlaceholderText(QCoreApplication.translate("AddStudent", u"\u0413\u0440\u0443\u043f\u043f\u0430...", None))
        self.semLabel1.setText(QCoreApplication.translate("AddStudent", u"\u0421\u0435\u043c\u0435\u0441\u0442\u0440 1:", None))
        self.semLabel2.setText(QCoreApplication.translate("AddStudent", u"\u0421\u0435\u043c\u0435\u0441\u0442\u0440 2:", None))
        self.semLabel3.setText(QCoreApplication.translate("AddStudent", u"\u0421\u0435\u043c\u0435\u0441\u0442\u0440 3:", None))
        self.semLabel4.setText(QCoreApplication.translate("AddStudent", u"\u0421\u0435\u043c\u0435\u0441\u0442\u0440 4:", None))
        self.semLabel5.setText(QCoreApplication.translate("AddStudent", u"\u0421\u0435\u043c\u0435\u0441\u0442\u0440 5:", None))
        self.semLabel6.setText(QCoreApplication.translate("AddStudent", u"\u0421\u0435\u043c\u0435\u0441\u0442\u0440 6:", None))
        self.semLabel7.setText(QCoreApplication.translate("AddStudent", u"\u0421\u0435\u043c\u0435\u0441\u0442\u0440 7:", None))
        self.semLabel8.setText(QCoreApplication.translate("AddStudent", u"\u0421\u0435\u043c\u0435\u0441\u0442\u0440 8:", None))
        self.semLabel9.setText(QCoreApplication.translate("AddStudent", u"\u0421\u0435\u043c\u0435\u0441\u0442\u0440 9:", None))
        self.semLabel10.setText(QCoreApplication.translate("AddStudent", u"\u0421\u0435\u043c\u0435\u0441\u0442\u0440 10:", None))
        self.backBtn.setText(QCoreApplication.translate("AddStudent", u"\u041d\u0430\u0437\u0430\u0434", None))
        self.addBtn.setText(QCoreApplication.translate("AddStudent", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0441\u0442\u0443\u0434\u0435\u043d\u0442\u0430", None))
    # retranslateUi

