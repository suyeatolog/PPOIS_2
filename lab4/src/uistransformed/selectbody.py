# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'selectbody.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
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
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(454, 446)
        Dialog.setMinimumSize(QSize(454, 446))
        Dialog.setMaximumSize(QSize(454, 446))
        self.consoleFrame = QFrame(Dialog)
        self.consoleFrame.setObjectName(u"consoleFrame")
        self.consoleFrame.setGeometry(QRect(0, 0, 451, 441))
        self.consoleFrame.setStyleSheet(u"QFrame#consoleFrame {\n"
"    border: 2px solid #555;\n"
"    border-radius: 10px;\n"
"    background-color: rgb(24, 26, 46);\n"
"    padding: 10px;\n"
"}")
        self.consoleFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.consoleFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.consoleWindowFrame = QFrame(self.consoleFrame)
        self.consoleWindowFrame.setObjectName(u"consoleWindowFrame")
        self.consoleWindowFrame.setGeometry(QRect(10, 20, 431, 401))
        self.consoleWindowFrame.setStyleSheet(u"QFrame#consoleWindowFrame {\n"
"    border: 2px solid #446b8a;\n"
"    border-radius: 10px;\n"
"    background-color: #141f2e;\n"
"    padding: 10px;\n"
"}")
        self.consoleWindowFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.consoleWindowFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.consoleWindowFrame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.selectbodyLabel = QLabel(self.consoleWindowFrame)
        self.selectbodyLabel.setObjectName(u"selectbodyLabel")
        self.selectbodyLabel.setMaximumSize(QSize(16777215, 40))
        self.selectbodyLabel.setStyleSheet(u"QLabel{\n"
"	\n"
"	background-color: rgb(20, 31, 46);\n"
"    color: #4cff4c;\n"
"    font-family: 'Courier New', monospace;\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"    qproperty-alignment: AlignCenter;\n"
"    padding: 10px;\n"
"    border-bottom: 1px solid #444;\n"
"}")

        self.verticalLayout.addWidget(self.selectbodyLabel)

        self.bodiesBox = QComboBox(self.consoleWindowFrame)
        self.bodiesBox.setObjectName(u"bodiesBox")
        self.bodiesBox.setStyleSheet(u"QComboBox {\n"
"    background-color: #1c2a3f;\n"
"    color: #a3cfff;\n"
"    border: 1px solid #3a5a7a;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    font-family: 'Courier New', monospace;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 20px;\n"
"    border-left: 1px solid #3a5a7a;\n"
"    border-top-right-radius: 5px;\n"
"    border-bottom-right-radius: 5px;\n"
"}\n"
"\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #1c2a3f;\n"
"    color: #a3cfff;\n"
"    selection-background-color: #2a3f5f;\n"
"    selection-color: #ffffff;\n"
"    border: 1px solid #3a5a7a;\n"
"    font-family: 'Courier New', monospace;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    border: 1px solid #6ba3d6;\n"
"}\n"
"\n"
"QComboBox:focus {\n"
"    border: 1px solid #a3cfff;\n"
"}")

        self.verticalLayout.addWidget(self.bodiesBox)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.travelBtn = QPushButton(self.consoleWindowFrame)
        self.travelBtn.setObjectName(u"travelBtn")
        self.travelBtn.setStyleSheet(u"QPushButton {\n"
"    background-color: #2a3f5f;\n"
"    color: #a3cfff;\n"
"    border: 2px solid #446b8a;\n"
"    border-radius: 8px;\n"
"    padding: 10px;\n"
"    font-family: 'Courier New', monospace;\n"
"    font-weight: bold;\n"
"    font-size: 14px;\n"
"    text-align: left;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #3a5f7f;\n"
"    border: 2px solid #6ba3d6;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #1d3047;\n"
"    border: 2px solid #a3cfff;\n"
"}")

        self.verticalLayout.addWidget(self.travelBtn)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.selectbodyLabel.setText(QCoreApplication.translate("Dialog", u"Select a body", None))
        self.travelBtn.setText(QCoreApplication.translate("Dialog", u"Travel", None))
    # retranslateUi

