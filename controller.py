# -*- coding: utf-8 -*-

from model import WebDriverHandler, GPACalculator
from view import View
from PySide6.QtWidgets import QTableWidgetItem
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

max_course_per_term = 15

class Controller:
    def __init__(self):
        self.driver_handler = WebDriverHandler()
        self.calculator = GPACalculator()

        self.view = View()

        self.view.main_window.button_delete_course.clicked.connect(self.view.delete_row)
        self.view.main_window.button_add_course.clicked.connect(self.view.add_row)
        self.view.main_window.button_calculate.clicked.connect(self.calculate)
        self.view.main_window.button_clear_table.clicked.connect(self.view.clear_table)
        self.view.main_window.button_pull.clicked.connect(self.pull)
        self.view.option_connect.triggered.connect(self.view.login)
        self.view.option_disconnect.triggered.connect(self.disconnect)
        self.view.login_window.button_login.clicked.connect(self.connect)
        self.view.main_window.show()

    def disconnect(self):
        self.driver_handler.close_driver()
        self.view.main_window.menu.setTitle("İTÜ ÖBS'ne Giriş Yap")
        self.view.main_window.button_pull.setEnabled(False)
        self.view.option_connect.setVisible(True)
        self.view.option_disconnect.setVisible(False)

    def connect(self):
        try:    
            if self.view.login_window.input_username.text() == "" or self.view.login_window.input_password.text() == "":
                raise Exception("Lütfen tüm alanları doldurunuz.")
            self.driver_handler.connect_to_system(self.view.login_window.input_username.text(), self.view.login_window.input_password.text())
            self.view.main_window.button_pull.setEnabled(True)
            self.view.login_window.close()
            self.view.main_window.menu.setTitle(f"Kullanıcı: {self.view.login_window.input_username.text()}")
            self.view.option_disconnect.setVisible(True)
            self.view.option_connect.setVisible(False)
        except Exception as e:
            print(e)
            self.view.show_error(f"Hata: {e}")
            self.driver_handler.close_driver()

    def add_to_table(self, course_dict):
        key_value_list = [(key, *value) for key, value in course_dict.items()]
        for row_index, x in enumerate(key_value_list):
            self.view.main_window.table.insertRow(row_index)
            for index, value in enumerate(x):
                item = QTableWidgetItem(value)
                self.view.main_window.table.setItem(row_index, index, item)


    def find_course_from_sis(self):
        self.driver_handler.driver.get("https://www.sis.itu.edu.tr/EN/student/undergraduate/course-information/course-information.php")
        for i in range(self.view.main_window.table.rowCount()):
            if i % 2 == 0:
                self.view.main_window.progressBar.setValue(self.view.main_window.progressBar.value() + 1)
            code_input = self.driver_handler.find_element_with_timeout(By.XPATH, "/html/body/div/div[2]/div/div[1]/form/div[1]/input")
            number_input = self.driver_handler.find_element_with_timeout(By.XPATH, "/html/body/div/div[2]/div/div[1]/form/div[2]/input")
            search_button = self.driver_handler.find_element_with_timeout(By.XPATH, "/html/body/div/div[2]/div/div[1]/form/input")
            code_input.clear()
            number_input.clear()
            course = self.view.main_window.table.item(i, 0).text()
            course_split = course.split(' ', 1)
            code_input.send_keys(course_split[0])
            number_input.send_keys(course_split[1])
            search_button.click()
            credit = self.driver_handler.find_element_with_timeout(By.XPATH, f'/html/body/div/div[2]/div/div[2]/table/tbody/tr/td/table[2]/tbody/tr[2]/td[1]').text
            if credit:
                item1 = QTableWidgetItem(credit)
                self.view.main_window.table.setItem(i, 3, item1)

    def pull(self):
        global max_course_per_term
        self.view.show_status(f"Dersler Kepler'den alınıyor...")
        self.view.main_window.progressBar.setEnabled(True)
        self.driver_handler.driver.get("https://kepler-beta.itu.edu.tr/ogrenci/NotBilgileri/DonemSonuNotlari")
        self.view.main_window.progressBar.setValue(0)
        
        pulled_course_dict = dict()
        menu_button = self.driver_handler.find_element_with_timeout(By.XPATH, f'/html/body/div/main/div[2]/div/div/div[2]/div/div/div/select')
        select = Select(menu_button)
        for i in range(len(select.options) - 1, -1, -1):
            self.view.main_window.progressBar.setValue(self.view.main_window.progressBar.value() + 5)
            try:
                select.select_by_index(i)
                for x in range(1, max_course_per_term + 1):
                    course_name = self.driver_handler.find_element_with_timeout(By.XPATH, f'/html/body/div/main/div[2]/div/div/div[3]/div/div/div/table/tbody/tr[{x}]/td[{2}]').text
                    pulled_course_dict[course_name] = []
                    for y in range(3, 5):
                        row_value = self.driver_handler.find_element_with_timeout(By.XPATH, f'/html/body/div/main/div[2]/div/div/div[3]/div/div/div/table/tbody/tr[{x}]/td[{y}]').text
                        pulled_course_dict[course_name].append(row_value)
            except:
                continue

        self.add_to_table(pulled_course_dict)
        self.view.main_window.progressBar.setValue(60)
        self.find_course_from_sis()
        self.view.main_window.progressBar.setValue(100)

        self.view.show_status(f"")
        self.view.main_window.progressBar.setEnabled(False)
        self.view.main_window.button_delete_course.setEnabled(True)
        self.view.main_window.button_calculate.setEnabled(True)
        self.view.main_window.button_clear_table.setEnabled(True)
        self.view.main_window.button_pull.setEnabled(False)

    def calculate(self):
        self.calculator.course_letter_grades.clear()
        self.calculator.course_credits.clear()
        for row in range(self.view.main_window.table.rowCount()):
            credit = self.view.main_window.table.item(row, 3)
            letter = self.view.main_window.table.item(row, 2)
            if credit is not None and letter is not None:
                if letter.text().upper() not in self.calculator.letter_grade_dict:
                    self.view.show_status("Lütfen uygun harf notu değerleri giriniz.")
                    return
                try:    
                    self.calculator.course_credits.append(float(credit.text()))
                except:
                    self.view.show_status("Lütfen uygun kredi değerleri giriniz.")
                    return
                self.calculator.course_letter_grades.append(letter.text().upper()) 
            else:
                 self.view.show_status("Lütfen tüm hücreleri doldurunuz.")
                 return
        self.view.show_status(f"Top. Ders: {self.view.main_window.table.rowCount()}, Top. Kredi: {sum(self.calculator.course_credits)}, Genel Ort.: {self.calculator.calculate_gpa():.2f}")