# -*- coding: utf-8 -*-

from model import Model
from view import Ui_main_window, Ui_window_login, Ui_Form
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QPushButton
from PySide6 import QtWidgets, QtGui
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)

from selenium.webdriver.edge.service import Service as EdgeService
from subprocess import CREATE_NO_WINDOW # This flag will only be available in windows

max_course_per_term = 15
max_term = 5

class Controller:
    def __init__(self):
        self.driver = None

        self.model = Model()
        self.main = QtWidgets.QMainWindow()
        self.main_window = Ui_main_window()
        self.main_window.setupUi(self.main)
        self.main.show()

        self.login = QtWidgets.QWidget()
        self.login_window = Ui_window_login()
        self.login_window.setupUi(self.login)

        self.error = QtWidgets.QWidget()
        self.error_window = Ui_Form()
        self.error_window.setupUi(self.error)

        self.main_window.button_add_course.clicked.connect(self.add_row)
        self.main_window.button_delete_course.clicked.connect(self.delete_row)
        self.main_window.button_calculate.clicked.connect(self.calculate)
        self.main_window.button_clear_table.clicked.connect(self.clear_table)
        self.main_window.button_pull.clicked.connect(self.pull)
        self.option_connect = QtGui.QAction("Sisteme bağlan", self.main)
        self.option_connect.triggered.connect(self.log_in)
        self.main_window.menu.addAction(self.option_connect)

        self.option_disconnect = QtGui.QAction("Bağlantıyı kes", self.main)
        self.option_disconnect.triggered.connect(self.disconnect)
        self.main_window.menu.addAction(self.option_disconnect)
        self.option_disconnect.setVisible(False)

        self.login_window.button_login.clicked.connect(self.connect)
        
        #self.main_window.button_pull.clicked.connect(self.pull)

    def show_error(self, message):
        self.error_window.label.setText(f"Hata: {message}")
        self.error.show()

    def log_in(self):
        self.login_window.input_password.setText("")
        self.login_window.input_username.setText("")
        self.login_window.input_pin.setText("")
        self.login.show()

    def disconnect(self):
        self.driver.close()
        self.driver = None
        self.main_window.menu.setTitle("İTÜ ÖBS'ne Giriş Yap")
        self.main_window.button_pull.setEnabled(False)
        self.option_connect.setVisible(True)
        self.option_disconnect.setVisible(False)

    def connect(self):
        edge_options = Options()
        edge_options.add_argument("--headless")
        if self.login_window.input_username.text() == "" or self.login_window.input_password.text() == "" or self.login_window.input_pin.text() == "":
            self.show_error("Lütfen tüm alanları doldurunuz.")
            return
        try:
            self.driver = webdriver.Edge(options=edge_options)
            self.driver.get("http://uzay.sis.itu.edu.tr/login/index.php")

            page_content = self.driver.page_source

            if "Tüm İTÜ hizmetleri" in page_content:
                username_input = self.driver.find_element("id", "ContentPlaceHolder1_tbUserName")
                password_input = self.driver.find_element("id", "ContentPlaceHolder1_tbPassword")
                login_button = self.driver.find_element("id", "ContentPlaceHolder1_btnLogin")
                
                username_input.send_keys(self.login_window.input_username.text())
                password_input.send_keys(self.login_window.input_password.text())
                login_button.click()

                page_content = self.driver.page_source
                
                if "Kullanıcı adı veya şifre hatalı." in page_content:
                    self.show_error("Kullanıcı adı ya da şifre hatalı.")
                    self.driver.close()

                else:
                    page_content_before = self.driver.page_source

                    pin_input = self.driver.find_element("name", "PIN")
                    pin_input.send_keys(self.login_window.input_pin.text())
                    login_obs = self.driver.find_element(By.XPATH, "/html/body/div[3]/form/p/input[1]")
                    login_obs.click()

                    page_content_after = self.driver.page_source
                    
                    if page_content_before == page_content_after:
                        self.error.show()
                        self.show_error("Pin hatalı.")
                        self.driver.close()
                    else:
                        ogrenci_servisi = self.driver.find_element(By.XPATH, "/html/body/div[3]/table[2]/tbody/tr[1]/td[2]/a")
                        ogrenci_servisi.click()
                        ogrenci_bilgileri = self.driver.find_element(By.XPATH, "/html/body/div[3]/table[1]/tbody/tr[2]/td[2]/a")
                        ogrenci_bilgileri.click()
                        transkript = self.driver.find_element(By.XPATH, "/html/body/div[3]/table[1]/tbody/tr[3]/td[2]/a")
                        transkript.click()
                        self.main_window.button_pull.setEnabled(True)
                        self.login.close()
                        self.main_window.menu.setTitle(f"Kullanıcı: {self.login_window.input_username.text()}")
                        self.option_disconnect.setVisible(True)
                        self.option_connect.setVisible(False)
        except:
            self.error.show()
            self.show_error("İTÜ ÖBS'ne ulaşılamadı.")
            self.driver.close()

    def pull(self):
        try:
            for z in range(2, 2 * max_term + 1):
                if z % 2 == 0:
                    for x in range(2, max_course_per_term):
                        self.main_window.table.insertRow(self.main_window.table.rowCount())
                        for y in range(1, 5):
                            try:
                                row_value = self.driver.find_element(By.XPATH, f"/html/body/div[3]/table/tbody/tr/td/table[2]/tbody/tr[{z}]/td[1]/table/tbody/tr[{x}]/td[{y}]/font").text
                                print(row_value)
                                
                                item1 = QTableWidgetItem(row_value)
                                self.main_window.table.setItem(self.main_window.table.rowCount() - 1, y - 1, item1)
                            except:
                                continue
                        if self.main_window.table.item(self.main_window.table.rowCount() - 1, 0) == None or self.main_window.table.item(self.main_window.table.rowCount() - 1, 3).text()[-1] == "*":
                            self.main_window.table.removeRow(self.main_window.table.rowCount() - 1)
            self.main_window.button_delete_course.setEnabled(True)
            self.main_window.button_calculate.setEnabled(True)
            self.main_window.button_clear_table.setEnabled(True)
            self.main_window.button_pull.setEnabled(False)
        except:
            self.show_error("Dersler çekilirken hatayla karşılaşıldı.")

    def add_row(self):
        self.main_window.table.insertRow(self.main_window.table.rowCount())
        if self.main_window.button_delete_course.isEnabled() == False:
            self.main_window.button_delete_course.setEnabled(True)
            self.main_window.button_calculate.setEnabled(True)
            self.main_window.button_clear_table.setEnabled(True)

    def delete_row(self):
        selected_ranges = self.main_window.table.selectedRanges()
        rows_to_delete = set()
        for selected_range in selected_ranges:
            top_row = selected_range.topRow()
            bottom_row = selected_range.bottomRow()
            rows_to_delete.update(range(top_row, bottom_row + 1))
        for row in sorted(rows_to_delete, reverse=True):
            self.main_window.table.removeRow(row)

        if self.main_window.table.rowCount() == 0:
            self.main_window.button_delete_course.setEnabled(False)
            self.main_window.button_clear_table.setEnabled(False)
            self.main_window.button_calculate.setEnabled(False)
            self.main_window.button_pull.setEnabled(True)

    def calculate(self):
        self.model.course_letter_grades.clear()
        self.model.course_credits.clear()
        for row in range(self.main_window.table.rowCount()):
            credit = self.main_window.table.item(row, 2)
            letter = self.main_window.table.item(row, 3)
            if credit is not None and letter is not None:
                if letter.text().upper() not in self.model.letter_grade_dict:
                    self.main_window.label.setText("Lütfen uygun harf notu değerleri giriniz.")
                    return
                try:    
                    self.model.course_credits.append(float(credit.text()))
                except:
                    self.main_window.label.setText("Lütfen uygun kredi değerleri giriniz.")
                    return
                self.model.course_letter_grades.append(letter.text().upper()) 
            else:
                 self.main_window.label.setText("Lütfen tüm hücreleri doldurunuz.")
                 return
        self.main_window.label.setText(f"Ortalama: {self.model.calculate_gpa():.2f}")
        
    def clear_table(self):
        self.main_window.table.setRowCount(0)
        self.main_window.button_delete_course.setEnabled(False)
        self.main_window.button_clear_table.setEnabled(False)
        self.main_window.button_pull.setEnabled(True)