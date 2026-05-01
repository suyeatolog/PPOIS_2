# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'showbodies.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(768, 645)
        Dialog.setMinimumSize(QSize(768, 645))
        Dialog.setMaximumSize(QSize(768, 645))
        Dialog.setStyleSheet(u"background-color: rgb(20, 31, 46);")
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.showBodiesLabel = QLabel(Dialog)
        self.showBodiesLabel.setObjectName(u"showBodiesLabel")
        self.showBodiesLabel.setStyleSheet(u"QLabel{\n"
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

        self.verticalLayout.addWidget(self.showBodiesLabel)

        self.listBodiesWidget = QListWidget(Dialog)
        self.listBodiesWidget.setObjectName(u"listBodiesWidget")
        self.listBodiesWidget.setStyleSheet(u"QListWidget {\n"
"    background-color: #141f2e;\n"
"    color: #a3cfff;\n"
"    border: 1px solid #3a5a7a;\n"
"    border-radius: 5px;\n"
"    font-family: 'Courier New', monospace;\n"
"    font-size: 14px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QListWidget::item {\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QListWidget::item:selected {\n"
"    background-color: #2a3f5f;\n"
"    color: #ffffff;\n"
"}\n"
"\n"
"QListWidget::item:hover {\n"
"    background-color: #1d3047;\n"
"}")

        self.verticalLayout.addWidget(self.listBodiesWidget)

        self.exit1Btn = QPushButton(Dialog)
        self.exit1Btn.setObjectName(u"exit1Btn")
        self.exit1Btn.setStyleSheet(u"QPushButton {\n"
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
"}\n"
"")

        self.verticalLayout.addWidget(self.exit1Btn)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.showBodiesLabel.setText(QCoreApplication.translate("Dialog", u"All celestial bodies", None))
        self.exit1Btn.setText(QCoreApplication.translate("Dialog", u"Exit", None))
    # retranslateUi

