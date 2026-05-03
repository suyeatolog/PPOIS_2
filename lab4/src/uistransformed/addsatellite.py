# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'addsatellite.ui'
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
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(462, 673)
        self.consoleFrame = QFrame(Dialog)
        self.consoleFrame.setObjectName(u"consoleFrame")
        self.consoleFrame.setGeometry(QRect(0, 0, 461, 671))
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
        self.consoleWindowFrame.setGeometry(QRect(7, 10, 448, 648))
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
        self.addAsteroidLabel = QLabel(self.consoleWindowFrame)
        self.addAsteroidLabel.setObjectName(u"addAsteroidLabel")
        self.addAsteroidLabel.setMaximumSize(QSize(16777215, 40))
        self.addAsteroidLabel.setStyleSheet(u"QLabel{\n"
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

        self.verticalLayout.addWidget(self.addAsteroidLabel)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.entername = QPushButton(self.consoleWindowFrame)
        self.entername.setObjectName(u"entername")
        self.entername.setMinimumSize(QSize(200, 0))
        self.entername.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout.addWidget(self.entername)

        self.nameEdit = QLineEdit(self.consoleWindowFrame)
        self.nameEdit.setObjectName(u"nameEdit")
        self.nameEdit.setMinimumSize(QSize(178, 30))
        self.nameEdit.setMaximumSize(QSize(178, 30))
        self.nameEdit.setStyleSheet(u"QLineEdit{\n"
"	\n"
"	background-color: rgb(20, 31, 46);\n"
"    color: #4cff4c;\n"
"    border: 1px solid #3a5a7a;\n"
"    border-radius: 5px;\n"
"    font-family: 'Courier New', monospace;\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"    qproperty-alignment: AlignCenter;\n"
"}")

        self.horizontalLayout.addWidget(self.nameEdit)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.selectplanet = QPushButton(self.consoleWindowFrame)
        self.selectplanet.setObjectName(u"selectplanet")
        self.selectplanet.setMinimumSize(QSize(200, 0))
        self.selectplanet.setMaximumSize(QSize(16777215, 16777215))
        self.selectplanet.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_2.addWidget(self.selectplanet)

        self.planetBox = QComboBox(self.consoleWindowFrame)
        self.planetBox.setObjectName(u"planetBox")
        self.planetBox.setMinimumSize(QSize(178, 0))
        self.planetBox.setMaximumSize(QSize(178, 16777215))
        self.planetBox.setStyleSheet(u"QComboBox {\n"
"    background-color: rgb(20, 31, 46);\n"
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

        self.horizontalLayout_2.addWidget(self.planetBox)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.enterperiod = QPushButton(self.consoleWindowFrame)
        self.enterperiod.setObjectName(u"enterperiod")
        self.enterperiod.setMinimumSize(QSize(200, 0))
        self.enterperiod.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_3.addWidget(self.enterperiod)

        self.orbitalEdit = QLineEdit(self.consoleWindowFrame)
        self.orbitalEdit.setObjectName(u"orbitalEdit")
        self.orbitalEdit.setMinimumSize(QSize(178, 30))
        self.orbitalEdit.setMaximumSize(QSize(178, 30))
        self.orbitalEdit.setStyleSheet(u"QLineEdit{\n"
"	\n"
"	background-color: rgb(20, 31, 46);\n"
"    color: #4cff4c;\n"
"    border: 1px solid #3a5a7a;\n"
"    border-radius: 5px;\n"
"    font-family: 'Courier New', monospace;\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"    qproperty-alignment: AlignCenter;\n"
"}")

        self.horizontalLayout_3.addWidget(self.orbitalEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.enterdistance = QPushButton(self.consoleWindowFrame)
        self.enterdistance.setObjectName(u"enterdistance")
        self.enterdistance.setMinimumSize(QSize(200, 0))
        self.enterdistance.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_10.addWidget(self.enterdistance)

        self.distanceEdit = QLineEdit(self.consoleWindowFrame)
        self.distanceEdit.setObjectName(u"distanceEdit")
        self.distanceEdit.setMinimumSize(QSize(178, 30))
        self.distanceEdit.setMaximumSize(QSize(178, 30))
        self.distanceEdit.setStyleSheet(u"QLineEdit{\n"
"	\n"
"	background-color: rgb(20, 31, 46);\n"
"    color: #4cff4c;\n"
"    border: 1px solid #3a5a7a;\n"
"    border-radius: 5px;\n"
"    font-family: 'Courier New', monospace;\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"    qproperty-alignment: AlignCenter;\n"
"}")

        self.horizontalLayout_10.addWidget(self.distanceEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.entermass = QPushButton(self.consoleWindowFrame)
        self.entermass.setObjectName(u"entermass")
        self.entermass.setMinimumSize(QSize(200, 0))
        self.entermass.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_4.addWidget(self.entermass)

        self.massEdit = QLineEdit(self.consoleWindowFrame)
        self.massEdit.setObjectName(u"massEdit")
        self.massEdit.setMinimumSize(QSize(178, 30))
        self.massEdit.setMaximumSize(QSize(178, 30))
        self.massEdit.setStyleSheet(u"QLineEdit{\n"
"	\n"
"	background-color: rgb(20, 31, 46);\n"
"    color: #4cff4c;\n"
"    border: 1px solid #3a5a7a;\n"
"    border-radius: 5px;\n"
"    font-family: 'Courier New', monospace;\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"    qproperty-alignment: AlignCenter;\n"
"}")

        self.horizontalLayout_4.addWidget(self.massEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.enterx = QPushButton(self.consoleWindowFrame)
        self.enterx.setObjectName(u"enterx")
        self.enterx.setMinimumSize(QSize(200, 0))
        self.enterx.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_5.addWidget(self.enterx)

        self.xEdit = QLineEdit(self.consoleWindowFrame)
        self.xEdit.setObjectName(u"xEdit")
        self.xEdit.setMinimumSize(QSize(178, 30))
        self.xEdit.setMaximumSize(QSize(178, 30))
        self.xEdit.setStyleSheet(u"QLineEdit{\n"
"	\n"
"	background-color: rgb(20, 31, 46);\n"
"    color: #4cff4c;\n"
"    border: 1px solid #3a5a7a;\n"
"    border-radius: 5px;\n"
"    font-family: 'Courier New', monospace;\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"    qproperty-alignment: AlignCenter;\n"
"}")

        self.horizontalLayout_5.addWidget(self.xEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.entery = QPushButton(self.consoleWindowFrame)
        self.entery.setObjectName(u"entery")
        self.entery.setMinimumSize(QSize(200, 0))
        self.entery.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_6.addWidget(self.entery)

        self.yEdit = QLineEdit(self.consoleWindowFrame)
        self.yEdit.setObjectName(u"yEdit")
        self.yEdit.setMinimumSize(QSize(178, 30))
        self.yEdit.setMaximumSize(QSize(178, 30))
        self.yEdit.setStyleSheet(u"QLineEdit{\n"
"	\n"
"	background-color: rgb(20, 31, 46);\n"
"    color: #4cff4c;\n"
"    border: 1px solid #3a5a7a;\n"
"    border-radius: 5px;\n"
"    font-family: 'Courier New', monospace;\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"    qproperty-alignment: AlignCenter;\n"
"}")

        self.horizontalLayout_6.addWidget(self.yEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.enterz = QPushButton(self.consoleWindowFrame)
        self.enterz.setObjectName(u"enterz")
        self.enterz.setMinimumSize(QSize(200, 0))
        self.enterz.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_7.addWidget(self.enterz)

        self.zEdit = QLineEdit(self.consoleWindowFrame)
        self.zEdit.setObjectName(u"zEdit")
        self.zEdit.setMinimumSize(QSize(178, 30))
        self.zEdit.setMaximumSize(QSize(178, 30))
        self.zEdit.setStyleSheet(u"QLineEdit{\n"
"	\n"
"	background-color: rgb(20, 31, 46);\n"
"    color: #4cff4c;\n"
"    border: 1px solid #3a5a7a;\n"
"    border-radius: 5px;\n"
"    font-family: 'Courier New', monospace;\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"    qproperty-alignment: AlignCenter;\n"
"}")

        self.horizontalLayout_7.addWidget(self.zEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.enterRadius = QPushButton(self.consoleWindowFrame)
        self.enterRadius.setObjectName(u"enterRadius")
        self.enterRadius.setMinimumSize(QSize(200, 0))
        self.enterRadius.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_8.addWidget(self.enterRadius)

        self.radiusEdit = QLineEdit(self.consoleWindowFrame)
        self.radiusEdit.setObjectName(u"radiusEdit")
        self.radiusEdit.setMinimumSize(QSize(178, 30))
        self.radiusEdit.setMaximumSize(QSize(178, 30))
        self.radiusEdit.setStyleSheet(u"QLineEdit{\n"
"	\n"
"	background-color: rgb(20, 31, 46);\n"
"    color: #4cff4c;\n"
"    border: 1px solid #3a5a7a;\n"
"    border-radius: 5px;\n"
"    font-family: 'Courier New', monospace;\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"    qproperty-alignment: AlignCenter;\n"
"}")

        self.horizontalLayout_8.addWidget(self.radiusEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.selectImageBtn = QPushButton(self.consoleWindowFrame)
        self.selectImageBtn.setObjectName(u"selectImageBtn")
        self.selectImageBtn.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout.addWidget(self.selectImageBtn)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
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

        self.horizontalLayout_9.addWidget(self.addSatelliteBtn)

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

        self.horizontalLayout_9.addWidget(self.exitBtn)


        self.verticalLayout.addLayout(self.horizontalLayout_9)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.addAsteroidLabel.setText(QCoreApplication.translate("Dialog", u"Add Satellite", None))
        self.entername.setText(QCoreApplication.translate("Dialog", u"Enter name:", None))
        self.selectplanet.setText(QCoreApplication.translate("Dialog", u"Select orbited planet", None))
        self.enterperiod.setText(QCoreApplication.translate("Dialog", u"Enter orbital period", None))
        self.enterdistance.setText(QCoreApplication.translate("Dialog", u"Enter distance", None))
        self.entermass.setText(QCoreApplication.translate("Dialog", u"Enter mass", None))
        self.enterx.setText(QCoreApplication.translate("Dialog", u"Enter X coordinate", None))
        self.entery.setText(QCoreApplication.translate("Dialog", u"Enter Y coordinate", None))
        self.enterz.setText(QCoreApplication.translate("Dialog", u"Enter Z coordinate", None))
        self.enterRadius.setText(QCoreApplication.translate("Dialog", u"Enter radius", None))
        self.selectImageBtn.setText(QCoreApplication.translate("Dialog", u"Select image", None))
        self.addSatelliteBtn.setText(QCoreApplication.translate("Dialog", u"Add", None))
        self.exitBtn.setText(QCoreApplication.translate("Dialog", u"Exit", None))
    # retranslateUi

