# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'controlspacecraft.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1206, 717)
        Dialog.setMinimumSize(QSize(1206, 717))
        Dialog.setMaximumSize(QSize(1206, 717))
        Dialog.setStyleSheet(u"background-color: rgb(24, 26, 46);")
        self.consoleFrame = QFrame(Dialog)
        self.consoleFrame.setObjectName(u"consoleFrame")
        self.consoleFrame.setGeometry(QRect(0, 0, 1201, 711))
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
        self.consoleWindowFrame.setGeometry(QRect(10, 20, 1181, 671))
        self.consoleWindowFrame.setStyleSheet(u"QFrame#consoleWindowFrame {\n"
"    border: 2px solid #446b8a;\n"
"    border-radius: 10px;\n"
"    background-color: #141f2e;\n"
"    padding: 10px;\n"
"}")
        self.consoleWindowFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.consoleWindowFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.consoleWindowFrame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.controlSpacecraftLabel = QLabel(self.consoleWindowFrame)
        self.controlSpacecraftLabel.setObjectName(u"controlSpacecraftLabel")
        self.controlSpacecraftLabel.setMaximumSize(QSize(16777215, 40))
        self.controlSpacecraftLabel.setStyleSheet(u"QLabel{\n"
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

        self.verticalLayout_3.addWidget(self.controlSpacecraftLabel)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.launchBtn = QPushButton(self.consoleWindowFrame)
        self.launchBtn.setObjectName(u"launchBtn")
        self.launchBtn.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout_3.addWidget(self.launchBtn)

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

        self.verticalLayout_3.addWidget(self.travelBtn)

        self.frame = QFrame(self.consoleWindowFrame)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.collectdataBtn = QPushButton(self.frame)
        self.collectdataBtn.setObjectName(u"collectdataBtn")
        self.collectdataBtn.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout.addWidget(self.collectdataBtn)

        self.resultLabel = QLabel(self.frame)
        self.resultLabel.setObjectName(u"resultLabel")
        self.resultLabel.setStyleSheet(u"QLabel{\n"
"	\n"
"	background-color: rgb(24, 26, 46);\n"
"    color: #4cff4c;\n"
"    font-family: 'Courier New', monospace;\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"    padding: 10px;\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.resultLabel)


        self.verticalLayout_3.addWidget(self.frame)

        self.frame_2 = QFrame(self.consoleWindowFrame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.resultLabel_2 = QLabel(self.frame_2)
        self.resultLabel_2.setObjectName(u"resultLabel_2")
        self.resultLabel_2.setStyleSheet(u"QLabel{\n"
"	\n"
"	background-color: rgb(24, 26, 46);\n"
"    color: #4cff4c;\n"
"    font-family: 'Courier New', monospace;\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"    padding: 10px;\n"
"}\n"
"")

        self.verticalLayout_2.addWidget(self.resultLabel_2)

        self.fuelupBtn = QPushButton(self.frame_2)
        self.fuelupBtn.setObjectName(u"fuelupBtn")
        self.fuelupBtn.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout_2.addWidget(self.fuelupBtn)


        self.verticalLayout_3.addWidget(self.frame_2)

        self.exit3Btn = QPushButton(self.consoleWindowFrame)
        self.exit3Btn.setObjectName(u"exit3Btn")
        self.exit3Btn.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout_3.addWidget(self.exit3Btn)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.controlSpacecraftLabel.setText(QCoreApplication.translate("Dialog", u"Control Spacecraft", None))
        self.launchBtn.setText(QCoreApplication.translate("Dialog", u"Launch Spacecraft", None))
        self.travelBtn.setText(QCoreApplication.translate("Dialog", u"Travel to another body", None))
        self.collectdataBtn.setText(QCoreApplication.translate("Dialog", u"Collect data", None))
        self.resultLabel.setText("")
        self.resultLabel_2.setText("")
        self.fuelupBtn.setText(QCoreApplication.translate("Dialog", u"Fuel up spacecraft", None))
        self.exit3Btn.setText(QCoreApplication.translate("Dialog", u"Exit", None))
    # retranslateUi

