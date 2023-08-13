# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_mainBfzVtH.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QLayout, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QSizePolicy,
    QWidget)

class Ui_main_window(object):
    def setupUi(self, main_window):
        if not main_window.objectName():
            main_window.setObjectName(u"main_window")
        main_window.setEnabled(True)
        main_window.resize(441, 528)
        icon = QIcon()
        icon.addFile(u"icons/favicon.ico", QSize(), QIcon.Normal, QIcon.Off)
        main_window.setWindowIcon(icon)
        self.centralwidget = QWidget(main_window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 30, 401, 451))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSpacing(25)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetNoConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.table = QTableWidget(self.verticalLayoutWidget)
        if (self.table.columnCount() < 4):
            self.table.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.table.setObjectName(u"table")
        self.table.setAlternatingRowColors(True)
        self.table.setShowGrid(True)
        self.table.setSortingEnabled(True)
        self.table.horizontalHeader().setVisible(True)
        self.table.verticalHeader().setVisible(False)
        self.table.verticalHeader().setHighlightSections(True)

        self.verticalLayout.addWidget(self.table)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(20)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setEnabled(True)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(15)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.button_clear_table = QPushButton(self.verticalLayoutWidget)
        self.button_clear_table.setObjectName(u"button_clear_table")
        self.button_clear_table.setEnabled(False)

        self.horizontalLayout.addWidget(self.button_clear_table)

        self.button_delete_course = QPushButton(self.verticalLayoutWidget)
        self.button_delete_course.setObjectName(u"button_delete_course")
        self.button_delete_course.setEnabled(False)

        self.horizontalLayout.addWidget(self.button_delete_course)

        self.button_add_course = QPushButton(self.verticalLayoutWidget)
        self.button_add_course.setObjectName(u"button_add_course")

        self.horizontalLayout.addWidget(self.button_add_course)


        self.verticalLayout_5.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(15)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.button_pull = QPushButton(self.verticalLayoutWidget)
        self.button_pull.setObjectName(u"button_pull")
        self.button_pull.setEnabled(False)

        self.horizontalLayout_3.addWidget(self.button_pull)

        self.button_calculate = QPushButton(self.verticalLayoutWidget)
        self.button_calculate.setObjectName(u"button_calculate")
        self.button_calculate.setEnabled(False)

        self.horizontalLayout_3.addWidget(self.button_calculate)


        self.verticalLayout_5.addLayout(self.horizontalLayout_3)


        self.verticalLayout_6.addLayout(self.verticalLayout_5)


        self.verticalLayout.addLayout(self.verticalLayout_6)

        main_window.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(main_window)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 441, 22))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu.setEnabled(True)
        main_window.setMenuBar(self.menubar)

        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(main_window)
        self.button_add_course.clicked.connect(self.button_add_course.showMenu)

        QMetaObject.connectSlotsByName(main_window)
    # setupUi

    def retranslateUi(self, main_window):
        main_window.setWindowTitle(QCoreApplication.translate("main_window", u"GPACalc", None))
        ___qtablewidgetitem = self.table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("main_window", u"Ders kodu", None));
        ___qtablewidgetitem1 = self.table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("main_window", u"Ders ad\u0131", None));
        ___qtablewidgetitem2 = self.table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("main_window", u"Kredi", None));
        ___qtablewidgetitem3 = self.table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("main_window", u"Harf notu", None));
        self.label.setText(QCoreApplication.translate("main_window", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\"><br/></span></p></body></html>", None))
        self.button_clear_table.setText(QCoreApplication.translate("main_window", u"Listeyi Temizle", None))
        self.button_delete_course.setText(QCoreApplication.translate("main_window", u"Se\u00e7ili Olanlar\u0131 Sil", None))
        self.button_add_course.setText(QCoreApplication.translate("main_window", u"Ders Ekle", None))
        self.button_pull.setText(QCoreApplication.translate("main_window", u"OBS'den Dersleri \u00c7ek", None))
        self.button_calculate.setText(QCoreApplication.translate("main_window", u"Ortalama Hesapla", None))
        self.menu.setTitle(QCoreApplication.translate("main_window", u"\u0130T\u00dc \u00d6BS'ne Giri\u015f Yap", None))
    # retranslateUi



class Ui_window_login(object):
    def setupUi(self, window_login):
        if not window_login.objectName():
            window_login.setObjectName(u"window_login")
        window_login.setWindowModality(Qt.WindowModal)
        window_login.resize(343, 161)
        icon = QIcon()
        icon.addFile(u"icons/login.ico", QSize(), QIcon.Normal, QIcon.Off)
        window_login.setWindowIcon(icon)
        window_login.setAutoFillBackground(False)
        self.input_username = QLineEdit(window_login)
        self.input_username.setObjectName(u"input_username")
        self.input_username.setGeometry(QRect(100, 20, 191, 21))
        self.input_password = QLineEdit(window_login)
        self.input_password.setObjectName(u"input_password")
        self.input_password.setGeometry(QRect(100, 50, 191, 21))
        self.input_password.setEchoMode(QLineEdit.Password)
        self.input_pin = QLineEdit(window_login)
        self.input_pin.setObjectName(u"input_pin")
        self.input_pin.setGeometry(QRect(100, 80, 191, 21))
        self.input_pin.setEchoMode(QLineEdit.Password)
        self.button_login = QPushButton(window_login)
        self.button_login.setObjectName(u"button_login")
        self.button_login.setGeometry(QRect(140, 120, 75, 24))
        self.label_username = QLabel(window_login)
        self.label_username.setObjectName(u"label_username")
        self.label_username.setGeometry(QRect(21, 21, 69, 16))
        self.label_username.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_password = QLabel(window_login)
        self.label_password.setObjectName(u"label_password")
        self.label_password.setGeometry(QRect(60, 50, 30, 16))
        self.label_password.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_password_2 = QLabel(window_login)
        self.label_password_2.setObjectName(u"label_password_2")
        self.label_password_2.setGeometry(QRect(70, 80, 19, 16))
        self.label_password_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.retranslateUi(window_login)

        QMetaObject.connectSlotsByName(window_login)
    # setupUi

    def retranslateUi(self, window_login):
        window_login.setWindowTitle(QCoreApplication.translate("window_login", u"\u0130T\u00dc \u00d6BS'ne Giri\u015f Yap", None))
        self.button_login.setText(QCoreApplication.translate("window_login", u"Giri\u015f Yap", None))
        self.label_username.setText(QCoreApplication.translate("window_login", u"Kullan\u0131c\u0131 ad\u0131: ", None))
        self.label_password.setText(QCoreApplication.translate("window_login", u"\u015eifre: ", None))
        self.label_password_2.setText(QCoreApplication.translate("window_login", u"Pin:", None))
    # retranslateUi

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(278, 129)
        icon = QIcon()
        icon.addFile(u"icons/error.ico", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        self.horizontalLayoutWidget = QWidget(Form)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 10, 261, 111))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Hata", None))
        self.label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\"></span></p></body></html>", None))
    # retranslateUi


