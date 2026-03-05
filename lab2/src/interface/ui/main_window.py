# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(840, 731)
        MainWindow.setStyleSheet(u"background-color: rgb(122, 122, 122);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_2 = QFrame(self.centralwidget)
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
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.mainTable = QTableWidget(self.frame_2)
        if (self.mainTable.columnCount() < 3):
            self.mainTable.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setBackground(QColor(213, 213, 213));
        self.mainTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setBackground(QColor(213, 213, 213));
        self.mainTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setBackground(QColor(213, 213, 213));
        self.mainTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.mainTable.setObjectName(u"mainTable")
        self.mainTable.setStyleSheet(u"QTableWidget {\n"
"    background-color: #f0f0f0;\n"
"    alternate-background-color: #e8e8e8;\n"
"    border: 2px solid #c0c0c0;\n"
"    border-radius: 10px;\n"
"    gridline-color: #dcdcdc;\n"
"    color: #333333;\n"
"    selection-background-color: #a0a0a0;\n"
"    selection-color: white;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #d3d3d3;\n"
"    padding: 4px;\n"
"    border: 1px solid #c0c0c0;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"/* \u0423\u0431\u0438\u0440\u0430\u0435\u043c \u043f\u0443\u043d\u043a\u0442\u0438\u0440\u043d\u0443\u044e \u0440\u0430\u043c\u043a\u0443 \u0432\u043e\u043a\u0440\u0443\u0433 \u044f\u0447\u0435\u0439\u043a\u0438 \u0432 \u0444\u043e\u043a\u0443\u0441\u0435 */\n"
"QTableWidget {\n"
"    outline: 0;\n"
"}\n"
"\n"
"QHeaderView {\n"
"    background-color: transparent;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QTableCornerButton::section {\n"
"    background-color: #d3d3d3;\n"
"    border: 1px solid #c0c0c0;\n"
"}")
        self.mainTable.setAlternatingRowColors(True)
        self.mainTable.setShowGrid(False)
        self.mainTable.setCornerButtonEnabled(False)

        self.verticalLayout_2.addWidget(self.mainTable)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.centralwidget)
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
        self.paginationSize = QComboBox(self.frame_3)
        self.paginationSize.addItem("")
        self.paginationSize.addItem("")
        self.paginationSize.addItem("")
        self.paginationSize.setObjectName(u"paginationSize")
        self.paginationSize.setMinimumSize(QSize(0, 30))
        self.paginationSize.setStyleSheet(u"QComboBox {\n"
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

        self.horizontalLayout_2.addWidget(self.paginationSize)

        self.firstPageBtn = QPushButton(self.frame_3)
        self.firstPageBtn.setObjectName(u"firstPageBtn")
        self.firstPageBtn.setStyleSheet(u"QPushButton {	\n"
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

        self.horizontalLayout_2.addWidget(self.firstPageBtn)

        self.previousArrowBtn = QPushButton(self.frame_3)
        self.previousArrowBtn.setObjectName(u"previousArrowBtn")
        self.previousArrowBtn.setStyleSheet(u"QPushButton {	\n"
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

        self.horizontalLayout_2.addWidget(self.previousArrowBtn)

        self.currentPageLabel = QLabel(self.frame_3)
        self.currentPageLabel.setObjectName(u"currentPageLabel")
        self.currentPageLabel.setStyleSheet(u"QLabel {\n"
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

        self.horizontalLayout_2.addWidget(self.currentPageLabel)

        self.nextArrowBtn = QPushButton(self.frame_3)
        self.nextArrowBtn.setObjectName(u"nextArrowBtn")
        self.nextArrowBtn.setStyleSheet(u"QPushButton {	\n"
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

        self.horizontalLayout_2.addWidget(self.nextArrowBtn)

        self.lastPageBtn = QPushButton(self.frame_3)
        self.lastPageBtn.setObjectName(u"lastPageBtn")
        self.lastPageBtn.setStyleSheet(u"QPushButton {	\n"
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

        self.horizontalLayout_2.addWidget(self.lastPageBtn)


        self.verticalLayout.addWidget(self.frame_3)

        self.frame = QFrame(self.centralwidget)
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
        self.addButton = QPushButton(self.frame)
        self.addButton.setObjectName(u"addButton")
        self.addButton.setMinimumSize(QSize(0, 50))
        self.addButton.setStyleSheet(u"QPushButton {	\n"
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

        self.horizontalLayout.addWidget(self.addButton)

        self.deleteButton = QPushButton(self.frame)
        self.deleteButton.setObjectName(u"deleteButton")
        self.deleteButton.setMinimumSize(QSize(0, 50))
        self.deleteButton.setStyleSheet(u"QPushButton {	\n"
"	background-color: rgb(119, 0, 33);\n"
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
"	background-color: rgb(203, 0, 29);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(119, 0, 33);\n"
"	border-style: inset;\n"
"}")

        self.horizontalLayout.addWidget(self.deleteButton)

        self.searchButton = QPushButton(self.frame)
        self.searchButton.setObjectName(u"searchButton")
        self.searchButton.setMinimumSize(QSize(0, 50))
        self.searchButton.setStyleSheet(u"QPushButton {	\n"
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

        self.horizontalLayout.addWidget(self.searchButton)


        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        ___qtablewidgetitem = self.mainTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0418\u041e \u0441\u0442\u0443\u0434\u0435\u043d\u0442\u0430", None));
        ___qtablewidgetitem1 = self.mainTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u0433\u0440\u0443\u043f\u043f\u0430", None));
        ___qtablewidgetitem2 = self.mainTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0449\u0435\u0441\u0442\u0432\u0435\u043d\u043d\u0430\u044f \u0440\u0430\u0431\u043e\u0442\u0430", None));
        self.paginationSize.setItemText(0, QCoreApplication.translate("MainWindow", u"5", None))
        self.paginationSize.setItemText(1, QCoreApplication.translate("MainWindow", u"10", None))
        self.paginationSize.setItemText(2, QCoreApplication.translate("MainWindow", u"15", None))

        self.firstPageBtn.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.previousArrowBtn.setText(QCoreApplication.translate("MainWindow", u"\u2190", None))
        self.currentPageLabel.setText(QCoreApplication.translate("MainWindow", u"current_page", None))
        self.nextArrowBtn.setText(QCoreApplication.translate("MainWindow", u"\u2192", None))
        self.lastPageBtn.setText(QCoreApplication.translate("MainWindow", u"last", None))
        self.addButton.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0437\u0430\u043f\u0438\u0441\u044c", None))
        self.deleteButton.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0435\u043d\u0438\u0435 \u0437\u0430\u043f\u0438\u0441\u0438", None))
        self.searchButton.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a \u0437\u0430\u043f\u0438\u0441\u0438", None))
    # retranslateUi

