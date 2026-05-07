# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'addcomet.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(462, 673)
        Dialog.setMinimumSize(QSize(462, 673))
        Dialog.setMaximumSize(QSize(462, 673))
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
        self.consoleWindowFrame.setGeometry(QRect(7, 10, 441, 650))
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

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.addAsteroidBtn = QPushButton(self.consoleWindowFrame)
        self.addAsteroidBtn.setObjectName(u"addAsteroidBtn")
        self.addAsteroidBtn.setEnabled(False)
        self.addAsteroidBtn.setMinimumSize(QSize(200, 0))
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

        self.horizontalLayout.addWidget(self.addAsteroidBtn)

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
        self.addCometBtn = QPushButton(self.consoleWindowFrame)
        self.addCometBtn.setObjectName(u"addCometBtn")
        self.addCometBtn.setEnabled(False)
        self.addCometBtn.setMinimumSize(QSize(200, 0))
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

        self.horizontalLayout_2.addWidget(self.addCometBtn)

        self.coreDiameterEdit = QLineEdit(self.consoleWindowFrame)
        self.coreDiameterEdit.setObjectName(u"coreDiameterEdit")
        self.coreDiameterEdit.setMinimumSize(QSize(178, 30))
        self.coreDiameterEdit.setMaximumSize(QSize(178, 30))
        self.coreDiameterEdit.setStyleSheet(u"QLineEdit{\n"
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

        self.horizontalLayout_2.addWidget(self.coreDiameterEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.addSatelliteBtn = QPushButton(self.consoleWindowFrame)
        self.addSatelliteBtn.setObjectName(u"addSatelliteBtn")
        self.addSatelliteBtn.setEnabled(False)
        self.addSatelliteBtn.setMinimumSize(QSize(200, 0))
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

        self.horizontalLayout_3.addWidget(self.addSatelliteBtn)

        self.tailLengthEdit = QLineEdit(self.consoleWindowFrame)
        self.tailLengthEdit.setObjectName(u"tailLengthEdit")
        self.tailLengthEdit.setMinimumSize(QSize(178, 30))
        self.tailLengthEdit.setMaximumSize(QSize(178, 30))
        self.tailLengthEdit.setStyleSheet(u"QLineEdit{\n"
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

        self.horizontalLayout_3.addWidget(self.tailLengthEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.addSatelliteBtn_2 = QPushButton(self.consoleWindowFrame)
        self.addSatelliteBtn_2.setObjectName(u"addSatelliteBtn_2")
        self.addSatelliteBtn_2.setEnabled(False)
        self.addSatelliteBtn_2.setMinimumSize(QSize(200, 0))
        self.addSatelliteBtn_2.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_10.addWidget(self.addSatelliteBtn_2)

        self.eccentricityEdit = QLineEdit(self.consoleWindowFrame)
        self.eccentricityEdit.setObjectName(u"eccentricityEdit")
        self.eccentricityEdit.setMinimumSize(QSize(178, 30))
        self.eccentricityEdit.setMaximumSize(QSize(178, 30))
        self.eccentricityEdit.setStyleSheet(u"QLineEdit{\n"
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

        self.horizontalLayout_10.addWidget(self.eccentricityEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.removeCometBtn = QPushButton(self.consoleWindowFrame)
        self.removeCometBtn.setObjectName(u"removeCometBtn")
        self.removeCometBtn.setEnabled(False)
        self.removeCometBtn.setMinimumSize(QSize(200, 0))
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

        self.horizontalLayout_4.addWidget(self.removeCometBtn)

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
        self.removeSatelliteBtn = QPushButton(self.consoleWindowFrame)
        self.removeSatelliteBtn.setObjectName(u"removeSatelliteBtn")
        self.removeSatelliteBtn.setEnabled(False)
        self.removeSatelliteBtn.setMinimumSize(QSize(200, 0))
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

        self.horizontalLayout_5.addWidget(self.removeSatelliteBtn)

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
        self.removeSatelliteBtn_2 = QPushButton(self.consoleWindowFrame)
        self.removeSatelliteBtn_2.setObjectName(u"removeSatelliteBtn_2")
        self.removeSatelliteBtn_2.setEnabled(False)
        self.removeSatelliteBtn_2.setMinimumSize(QSize(200, 0))
        self.removeSatelliteBtn_2.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_6.addWidget(self.removeSatelliteBtn_2)

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
        self.removeSatelliteBtn_3 = QPushButton(self.consoleWindowFrame)
        self.removeSatelliteBtn_3.setObjectName(u"removeSatelliteBtn_3")
        self.removeSatelliteBtn_3.setEnabled(False)
        self.removeSatelliteBtn_3.setMinimumSize(QSize(200, 0))
        self.removeSatelliteBtn_3.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_7.addWidget(self.removeSatelliteBtn_3)

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
        self.removeSatelliteBtn_4 = QPushButton(self.consoleWindowFrame)
        self.removeSatelliteBtn_4.setObjectName(u"removeSatelliteBtn_4")
        self.removeSatelliteBtn_4.setEnabled(False)
        self.removeSatelliteBtn_4.setMinimumSize(QSize(200, 0))
        self.removeSatelliteBtn_4.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_8.addWidget(self.removeSatelliteBtn_4)

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
        self.addCometBtn_2 = QPushButton(self.consoleWindowFrame)
        self.addCometBtn_2.setObjectName(u"addCometBtn_2")
        self.addCometBtn_2.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_9.addWidget(self.addCometBtn_2)

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
        self.addAsteroidLabel.setText(QCoreApplication.translate("Dialog", u"Add Comet", None))
        self.addAsteroidBtn.setText(QCoreApplication.translate("Dialog", u"Enter name:", None))
        self.addCometBtn.setText(QCoreApplication.translate("Dialog", u"Enter core diameter:", None))
        self.addSatelliteBtn.setText(QCoreApplication.translate("Dialog", u"Enter tail length:", None))
        self.addSatelliteBtn_2.setText(QCoreApplication.translate("Dialog", u"Enter eccentricity:", None))
        self.removeCometBtn.setText(QCoreApplication.translate("Dialog", u"Enter mass", None))
        self.removeSatelliteBtn.setText(QCoreApplication.translate("Dialog", u"Enter X coordinate", None))
        self.removeSatelliteBtn_2.setText(QCoreApplication.translate("Dialog", u"Enter Y coordinate", None))
        self.removeSatelliteBtn_3.setText(QCoreApplication.translate("Dialog", u"Enter Z coordinate", None))
        self.removeSatelliteBtn_4.setText(QCoreApplication.translate("Dialog", u"Enter radius", None))
        self.selectImageBtn.setText(QCoreApplication.translate("Dialog", u"Select image", None))
        self.addCometBtn_2.setText(QCoreApplication.translate("Dialog", u"Add", None))
        self.exitBtn.setText(QCoreApplication.translate("Dialog", u"Exit", None))
    # retranslateUi

