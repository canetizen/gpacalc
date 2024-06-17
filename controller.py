# -*- coding: utf-8 -*-

from model import Model
from view import View
from PySide6.QtWidgets import QTableWidgetItem
from PySide6 import QtGui
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select



class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View()

        self.view.main_window.show()

        self.view.main_window.button_delete_course.clicked.connect(self.delete_row)
        self.view.main_window.button_add_course.clicked.connect(self.add_row)
        self.view.main_window.button_calculate.clicked.connect(self.calculate)
        self.view.main_window.button_clear_table.clicked.connect(self.clear_table)
        self.view.main_window.button_pull.clicked.connect(self.pull)
        self.option_connect = QtGui.QAction("Sisteme bağlan", self.view.main_window)
        self.option_connect.triggered.connect(self.log_in)
        self.view.main_window.menu.addAction(self.option_connect)

        self.option_disconnect = QtGui.QAction("Bağlantıyı kes", self.view.main_window)
        self.option_disconnect.triggered.connect(self.disconnect)
        self.view.main_window.menu.addAction(self.option_disconnect)
        self.option_disconnect.setVisible(False)

        self.view.login_window.button_login.clicked.connect(self.connect)

    def show_error(self, message):
        self.view.error_window.label.setText(f"Hata: {message}")
        self.view.error_window.show()

    def log_in(self):
        self.view.login_window.button_login.setEnabled(True)
        self.view.login_window.input_password.setText("")
        self.view.login_window.input_username.setText("")
        self.view.login_window.show()

    def disconnect(self):
        self.model.driver.close()
        self.view.main_window.menu.setTitle("İTÜ ÖBS'ne Giriş Yap")
        self.view.main_window.button_pull.setEnabled(False)
        self.option_connect.setVisible(True)
        self.option_disconnect.setVisible(False)

    def connect(self):
        if self.view.login_window.input_username.text() == "" or self.view.login_window.input_password.text() == "":
            self.show_error("Lütfen tüm alanları doldurunuz.")
            return
        else:
            result = self.model.connect_to_system(self.view.login_window.input_username.text(), self.view.login_window.input_password.text())
            if result != "":
                self.view.error_window.label.setText(result)
                self.view.error_window.show()
            else:
                self.view.main_window.button_pull.setEnabled(True)
                self.view.login_window.close()
                self.view.main_window.menu.setTitle(f"Kullanıcı: {self.view.login_window.input_username.text()}")
                self.option_disconnect.setVisible(True)
                self.option_connect.setVisible(False)

    def add_to_table(self, course_dict):
        key_value_list = [(key, *value) for key, value in course_dict.items()]
        for row_index, x in enumerate(key_value_list):
            self.view.main_window.table.insertRow(row_index)
            for index, value in enumerate(x):
                item = QTableWidgetItem(value)
                self.view.main_window.table.setItem(row_index, index, item)


    def find_course_from_sis(self):
        self.model.driver.get("https://www.sis.itu.edu.tr/EN/student/undergraduate/course-information/course-information.php")
        for i in range(self.view.main_window.table.rowCount()):
            if i % 2 == 0:
                self.view.main_window.progressBar.setValue(self.view.main_window.progressBar.value() + 1)
            code_input = self.model.find_element_with_timeout(By.XPATH, "/html/body/div/div[2]/div/div[1]/form/div[1]/input")
            number_input = self.model.find_element_with_timeout(By.XPATH, "/html/body/div/div[2]/div/div[1]/form/div[2]/input")
            search_button = self.model.find_element_with_timeout(By.XPATH, "/html/body/div/div[2]/div/div[1]/form/input")
            if None in (code_input, number_input, search_button):
                continue
            code_input.clear()
            number_input.clear()
            course = self.view.main_window.table.item(i, 0).text()
            course_split = course.split(' ', 1)
            code_input.send_keys(course_split[0])
            number_input.send_keys(course_split[1])
            search_button.click()
            credit = self.model.find_element_with_timeout(By.XPATH, f'/html/body/div/div[2]/div/div[2]/table/tbody/tr/td/table[2]/tbody/tr[2]/td[1]').text
            if credit:
                item1 = QTableWidgetItem(credit)
                self.view.main_window.table.setItem(i, 3, item1)

    def pull(self):
        self.view.main_window.label.setText(f"Dersler Kepler'den alınıyor...")
        self.view.main_window.progressBar.setEnabled(True)
        self.model.driver.get("https://kepler-beta.itu.edu.tr/ogrenci/NotBilgileri/DonemSonuNotlari")
        self.view.main_window.progressBar.setValue(0)
        max_course_per_term = 15
        max_term = 8
        pulled_course_dict = dict()
        for i in range(max_term - 1, -1, -1):
            try:
                menu_button = self.model.find_element_with_timeout(By.XPATH, f'/html/body/div/main/div[2]/div/div/div[2]/div/div/div/select')
                if not menu_button:
                    continue
                select = Select(menu_button)
                select.select_by_index(i)
                for x in range(1, max_course_per_term + 1):
                    course_name = self.model.find_element_with_timeout(By.XPATH, f'/html/body/div/main/div[2]/div/div/div[3]/div/div/div/table/tbody/tr[{x}]/td[{2}]').text
                    pulled_course_dict[course_name] = []
                    for y in range(3, 5):
                        row_value = self.model.find_element_with_timeout(By.XPATH, f'/html/body/div/main/div[2]/div/div/div[3]/div/div/div/table/tbody/tr[{x}]/td[{y}]').text
                        pulled_course_dict[course_name].append(row_value)
                self.view.main_window.progressBar.setValue(self.view.main_window.progressBar.value() + 5)
            except:
                self.view.main_window.progressBar.setValue(self.view.main_window.progressBar.value() + 5)
                continue

        self.add_to_table(pulled_course_dict)
        self.view.main_window.progressBar.setValue(60)
        self.find_course_from_sis()
        self.view.main_window.progressBar.setValue(100)

        self.view.main_window.progressBar.setEnabled(False)
        self.view.main_window.button_delete_course.setEnabled(True)
        self.view.main_window.button_calculate.setEnabled(True)
        self.view.main_window.button_clear_table.setEnabled(True)
        self.view.main_window.button_pull.setEnabled(False)


 
    def add_row(self):
        self.view.main_window.table.insertRow(self.view.main_window.table.rowCount())
        if self.view.main_window.button_delete_course.isEnabled() == False:
            self.view.main_window.button_delete_course.setEnabled(True)
            self.view.main_window.button_calculate.setEnabled(True)
            self.view.main_window.button_clear_table.setEnabled(True)
        self.view.main_window.label.setText("")

    def delete_row(self):
        selected_ranges = self.view.main_window.table.selectedRanges()
        rows_to_delete = set()
        for selected_range in selected_ranges:
            top_row = selected_range.topRow()
            bottom_row = selected_range.bottomRow()
            rows_to_delete.update(range(top_row, bottom_row + 1))
        for row in sorted(rows_to_delete, reverse=True):
            self.view.main_window.table.removeRow(row)

        if self.view.main_window.table.rowCount() == 0:
            self.view.main_window.button_delete_course.setEnabled(False)
            self.view.main_window.button_clear_table.setEnabled(False)
            self.view.main_window.button_calculate.setEnabled(False)
            self.view.main_window.button_pull.setEnabled(True)
        self.view.main_window.label.setText("")

    def calculate(self):
        self.model.course_letter_grades.clear()
        self.model.course_credits.clear()
        for row in range(self.view.main_window.table.rowCount()):
            credit = self.view.main_window.table.item(row, 3)
            letter = self.view.main_window.table.item(row, 2)
            if credit is not None and letter is not None:
                if letter.text().upper() not in self.model.letter_grade_dict:
                    self.view.main_window.label.setText("Lütfen uygun harf notu değerleri giriniz.")
                    return
                try:    
                    self.model.course_credits.append(float(credit.text()))
                except:
                    self.view.main_window.label.setText("Lütfen uygun kredi değerleri giriniz.")
                    return
                self.model.course_letter_grades.append(letter.text().upper()) 
            else:
                 self.view.main_window.label.setText("Lütfen tüm hücreleri doldurunuz.")
                 return
        self.view.main_window.label.setText(f"Toplam Ders: {self.view.main_window.table.rowCount()}, Ortalama: {self.model.calculate_gpa():.2f}")
        
    def clear_table(self):
        self.view.main_window.table.setRowCount(0)
        self.view.main_window.button_delete_course.setEnabled(False)
        self.view.main_window.button_clear_table.setEnabled(False)
        self.view.main_window.button_pull.setEnabled(True)
        self.view.main_window.button_calculate.setEnabled(False)
        self.view.main_window.label.setText("")

        