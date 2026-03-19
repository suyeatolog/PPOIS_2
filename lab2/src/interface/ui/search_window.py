# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'searchWindow.ui'
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
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpinBox, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_SearchStudent(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1118, 461)
        Dialog.setStyleSheet(u"background-color: rgb(122, 122, 122);")
        self.verticalLayout_4 = QVBoxLayout(Dialog)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.searchLabel = QLabel(Dialog)
        self.searchLabel.setObjectName(u"searchLabel")
        self.searchLabel.setMaximumSize(QSize(16777215, 50))
        self.searchLabel.setStyleSheet(u"QLabel {\n"
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

        self.verticalLayout_4.addWidget(self.searchLabel)

        self.frame_7 = QFrame(Dialog)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setStyleSheet(u"QFrame {\n"
"    background-color: rgba(255, 255, 255, 30); \n"
"    border-radius: 10px;\n"
"    border: 1px solid rgba(255, 255, 255, 50);\n"
"}\n"
"\n"
"QTableWidget {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    gridline-color: rgba(255, 255, 255, 20);\n"
"}")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.frame_6 = QFrame(self.frame_7)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(700, 0))
        self.frame_6.setStyleSheet(u"QFrame {\n"
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
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.searchResultTable = QTableWidget(self.frame_6)
        if (self.searchResultTable.columnCount() < 3):
            self.searchResultTable.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setBackground(QColor(213, 213, 213));
        self.searchResultTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setBackground(QColor(213, 213, 213));
        self.searchResultTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setBackground(QColor(213, 213, 213));
        self.searchResultTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.searchResultTable.setObjectName(u"searchResultTable")
        self.searchResultTable.setStyleSheet(u"QTableWidget {\n"
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
        self.searchResultTable.setAlternatingRowColors(True)
        self.searchResultTable.setShowGrid(False)
        self.searchResultTable.setCornerButtonEnabled(False)

        self.verticalLayout_2.addWidget(self.searchResultTable)

        self.frame_5 = QFrame(self.frame_6)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"QFrame {\n"
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
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.paginationSize = QComboBox(self.frame_5)
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
"}\n"
"\n"
"QComboBox:focus {\n"
"    border: 2px solid #3498db;\n"
"    background-color: #ffffff;\n"
"}")

        self.horizontalLayout_4.addWidget(self.paginationSize)

        self.firstPageBtn = QPushButton(self.frame_5)
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

        self.horizontalLayout_4.addWidget(self.firstPageBtn)

        self.previousArrowBtn = QPushButton(self.frame_5)
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

        self.horizontalLayout_4.addWidget(self.previousArrowBtn)

        self.currentPageLabel = QLabel(self.frame_5)
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

        self.horizontalLayout_4.addWidget(self.currentPageLabel)

        self.nextArrowBtn = QPushButton(self.frame_5)
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

        self.horizontalLayout_4.addWidget(self.nextArrowBtn)

        self.lastPageBtn = QPushButton(self.frame_5)
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

        self.horizontalLayout_4.addWidget(self.lastPageBtn)


        self.verticalLayout_2.addWidget(self.frame_5)


        self.horizontalLayout_5.addWidget(self.frame_6)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame = QFrame(self.frame_7)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(200, 0))
        self.frame.setMaximumSize(QSize(400, 16777215))
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
"    qproperty-alignment: 'AlignCenter';\n"
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
        self.frame_4.setMaximumSize(QSize(16777215, 50))
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


        self.verticalLayout_3.addWidget(self.frame)

        self.frame_3 = QFrame(self.frame_7)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(400, 75))
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

        self.horizontalLayout.addWidget(self.backBtn)

        self.searchBtn = QPushButton(self.frame_3)
        self.searchBtn.setObjectName(u"searchBtn")
        self.searchBtn.setStyleSheet(u"QPushButton {	\n"
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

        self.horizontalLayout.addWidget(self.searchBtn)


        self.verticalLayout_3.addWidget(self.frame_3)


        self.horizontalLayout_5.addLayout(self.verticalLayout_3)


        self.verticalLayout_4.addWidget(self.frame_7)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.searchLabel.setText(QCoreApplication.translate("Dialog", u"\u041f\u043e\u0438\u0441\u043a \u0441\u0442\u0443\u0434\u0435\u043d\u0442\u043e\u0432", None))
        ___qtablewidgetitem = self.searchResultTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog", u"\u0424\u0418\u041e \u0441\u0442\u0443\u0434\u0435\u043d\u0442\u0430", None));
        ___qtablewidgetitem1 = self.searchResultTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dialog", u"\u0433\u0440\u0443\u043f\u043f\u0430", None));
        ___qtablewidgetitem2 = self.searchResultTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Dialog", u"\u041e\u0431\u0449\u0435\u0441\u0442\u0432\u0435\u043d\u043d\u0430\u044f \u0440\u0430\u0431\u043e\u0442\u0430", None));
        self.paginationSize.setItemText(0, QCoreApplication.translate("Dialog", u"5", None))
        self.paginationSize.setItemText(1, QCoreApplication.translate("Dialog", u"10", None))
        self.paginationSize.setItemText(2, QCoreApplication.translate("Dialog", u"15", None))

        self.firstPageBtn.setText(QCoreApplication.translate("Dialog", u"1", None))
        self.previousArrowBtn.setText(QCoreApplication.translate("Dialog", u"\u2190", None))
        self.currentPageLabel.setText(QCoreApplication.translate("Dialog", u"current_page", None))
        self.nextArrowBtn.setText(QCoreApplication.translate("Dialog", u"\u2192", None))
        self.lastPageBtn.setText(QCoreApplication.translate("Dialog", u"last", None))
        self.lastName.setText("")
        self.lastName.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0444\u0430\u043c\u0438\u043b\u0438\u044e...", None))
        self.groupBox.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u0413\u0440\u0443\u043f\u043f\u0430...", None))
        self.socialWorkLabel.setText(QCoreApplication.translate("Dialog", u"\u041e\u0431\u0449\u0435\u0441\u0442\u0432\u0435\u043d\u043d\u0430\u044f \u0440\u0430\u0431\u043e\u0442\u0430", None))
        self.backBtn.setText(QCoreApplication.translate("Dialog", u"\u041d\u0430\u0437\u0430\u0434", None))
        self.searchBtn.setText(QCoreApplication.translate("Dialog", u"\u041d\u0430\u0439\u0442\u0438 \u0441\u0442\u0443\u0434\u0435\u043d\u0442\u043e\u0432", None))
    # retranslateUi

