# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1430, 785)
        MainWindow.setMinimumSize(QSize(1430, 785))
        MainWindow.setMaximumSize(QSize(1430, 785))
        MainWindow.setStyleSheet(u"background-color: rgb(40, 44, 78);\n"
"border-color: rgb(63, 70, 123);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.objectDisplayFrame = QFrame(self.centralwidget)
        self.objectDisplayFrame.setObjectName(u"objectDisplayFrame")
        self.objectDisplayFrame.setGeometry(QRect(510, 20, 901, 711))
        self.objectDisplayFrame.setStyleSheet(u"QFrame#objectDisplayFrame {\n"
"    border: 2px solid #555;\n"
"    border-radius: 10px;\n"
"    background-color: rgb(24, 26, 46);\n"
"    padding: 10px;\n"
"}\n"
"\n"
"QLabel#objectImageLabel {\n"
"    background-color: #111;\n"
"    border: 1px solid #444;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QLabel#objectNameLabel {\n"
"	\n"
"	background-color: rgb(24, 26, 46);\n"
"    color: #4cff4c;\n"
"    font-family: 'Courier New', monospace;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"    qproperty-alignment: AlignCenter;\n"
"}")
        self.objectDisplayFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.objectDisplayFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.objectDisplayFrame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.objectImageLabel = QLabel(self.objectDisplayFrame)
        self.objectImageLabel.setObjectName(u"objectImageLabel")
        self.objectImageLabel.setMinimumSize(QSize(0, 630))

        self.verticalLayout.addWidget(self.objectImageLabel)

        self.objectNameLabel = QLabel(self.objectDisplayFrame)
        self.objectNameLabel.setObjectName(u"objectNameLabel")

        self.verticalLayout.addWidget(self.objectNameLabel)

        self.consoleFrame = QFrame(self.centralwidget)
        self.consoleFrame.setObjectName(u"consoleFrame")
        self.consoleFrame.setGeometry(QRect(30, 20, 451, 711))
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
        self.verticalLayout_2 = QVBoxLayout(self.consoleWindowFrame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.consoleTitleLabel = QLabel(self.consoleWindowFrame)
        self.consoleTitleLabel.setObjectName(u"consoleTitleLabel")
        self.consoleTitleLabel.setMaximumSize(QSize(16777215, 40))
        self.consoleTitleLabel.setStyleSheet(u"QLabel#consoleTitleLabel {\n"
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

        self.verticalLayout_2.addWidget(self.consoleTitleLabel)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.showBtn = QPushButton(self.consoleWindowFrame)
        self.showBtn.setObjectName(u"showBtn")
        self.showBtn.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout_2.addWidget(self.showBtn)

        self.celestialCtrlBtn = QPushButton(self.consoleWindowFrame)
        self.celestialCtrlBtn.setObjectName(u"celestialCtrlBtn")
        self.celestialCtrlBtn.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout_2.addWidget(self.celestialCtrlBtn)

        self.spaceshipCtrlBtn = QPushButton(self.consoleWindowFrame)
        self.spaceshipCtrlBtn.setObjectName(u"spaceshipCtrlBtn")
        self.spaceshipCtrlBtn.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout_2.addWidget(self.spaceshipCtrlBtn)

        self.exitBtn = QPushButton(self.consoleWindowFrame)
        self.exitBtn.setObjectName(u"exitBtn")
        self.exitBtn.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout_2.addWidget(self.exitBtn)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.objectImageLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.objectNameLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.consoleTitleLabel.setText(QCoreApplication.translate("MainWindow", u"CONSOLE", None))
        self.showBtn.setText(QCoreApplication.translate("MainWindow", u"Show all celestial bodies", None))
        self.celestialCtrlBtn.setText(QCoreApplication.translate("MainWindow", u"Add/remove celestial bodies", None))
        self.spaceshipCtrlBtn.setText(QCoreApplication.translate("MainWindow", u"Control spacecraft", None))
        self.exitBtn.setText(QCoreApplication.translate("MainWindow", u"exit", None))
    # retranslateUi

