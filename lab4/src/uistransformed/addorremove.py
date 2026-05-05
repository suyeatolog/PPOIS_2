# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'addorremove.ui'
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
        Dialog.resize(452, 712)
        Dialog.setMinimumSize(QSize(452, 712))
        Dialog.setMaximumSize(QSize(452, 712))
        self.consoleFrame = QFrame(Dialog)
        self.consoleFrame.setObjectName(u"consoleFrame")
        self.consoleFrame.setGeometry(QRect(0, 0, 451, 711))
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
        self.consoleWindowFrame.setGeometry(QRect(10, 10, 431, 691))
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
        self.console2TitleLabel = QLabel(self.consoleWindowFrame)
        self.console2TitleLabel.setObjectName(u"console2TitleLabel")
        self.console2TitleLabel.setMaximumSize(QSize(16777215, 40))
        self.console2TitleLabel.setStyleSheet(u"QLabel{\n"
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

        self.verticalLayout.addWidget(self.console2TitleLabel)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.addAsteroidBtn = QPushButton(self.consoleWindowFrame)
        self.addAsteroidBtn.setObjectName(u"addAsteroidBtn")
        self.addAsteroidBtn.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout.addWidget(self.addAsteroidBtn)

        self.addCometBtn = QPushButton(self.consoleWindowFrame)
        self.addCometBtn.setObjectName(u"addCometBtn")
        self.addCometBtn.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout.addWidget(self.addCometBtn)

        self.addSatelliteBtn = QPushButton(self.consoleWindowFrame)
        self.addSatelliteBtn.setObjectName(u"addSatelliteBtn")
        self.addSatelliteBtn.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout.addWidget(self.addSatelliteBtn)

        self.removeAsteroidBtn = QPushButton(self.consoleWindowFrame)
        self.removeAsteroidBtn.setObjectName(u"removeAsteroidBtn")
        self.removeAsteroidBtn.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout.addWidget(self.removeAsteroidBtn)

        self.removeCometBtn = QPushButton(self.consoleWindowFrame)
        self.removeCometBtn.setObjectName(u"removeCometBtn")
        self.removeCometBtn.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout.addWidget(self.removeCometBtn)

        self.removeSatelliteBtn = QPushButton(self.consoleWindowFrame)
        self.removeSatelliteBtn.setObjectName(u"removeSatelliteBtn")
        self.removeSatelliteBtn.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout.addWidget(self.removeSatelliteBtn)

        self.exit2Btn = QPushButton(self.consoleWindowFrame)
        self.exit2Btn.setObjectName(u"exit2Btn")
        self.exit2Btn.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout.addWidget(self.exit2Btn)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.console2TitleLabel.setText(QCoreApplication.translate("Dialog", u"Add/remove celestial bodies", None))
        self.addAsteroidBtn.setText(QCoreApplication.translate("Dialog", u"Add asteroid", None))
        self.addCometBtn.setText(QCoreApplication.translate("Dialog", u"Add comet", None))
        self.addSatelliteBtn.setText(QCoreApplication.translate("Dialog", u"Add satellite", None))
        self.removeAsteroidBtn.setText(QCoreApplication.translate("Dialog", u"Remove asteroid", None))
        self.removeCometBtn.setText(QCoreApplication.translate("Dialog", u"Remove comet", None))
        self.removeSatelliteBtn.setText(QCoreApplication.translate("Dialog", u"Remove satellite", None))
        self.exit2Btn.setText(QCoreApplication.translate("Dialog", u"Exit", None))
    # retranslateUi

