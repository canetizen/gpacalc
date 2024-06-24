from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class GPACalculator:
    def __init__(self):
        self.course_letter_grades = []
        self.course_credits = []
        self.letter_grade_dict = {
            "AA": 4.0, "BA": 3.5, "BA+": 3.75, "BB": 3.0, "BB+": 3.25, 
            "CB": 2.5, "CB+": 2.75, "CC": 2.0, "CC+": 2.25, 
            "DC": 1.5, "DC+": 1.75, "DD": 1.0, "DD+": 1.25, 
            "FF": 0.0, "VF": 0.0, "BL": 0.0, "BZ": 0.0
        }

    def calculate_gpa(self):
        total = sum(self.letter_grade_dict.get(grade, 0) * float(credit)
                    for grade, credit in zip(self.course_letter_grades, self.course_credits))
        total_credits = sum(float(credit) for credit in self.course_credits)
        return total / total_credits if total_credits else 0.0

    def add_course(self, grade, credit):
        self.course_letter_grades.append(grade)
        self.course_credits.append(credit)

class WebDriverHandler:
    def __init__(self):
        self.driver = None

    def setup_driver(self, headless=True): # To turn off browser view, set it to False.
        options = Options()
        if headless:
            options.add_argument("--headless")
        options.profile = webdriver.FirefoxProfile()
        driver_path = "/snap/bin/firefox.geckodriver"
        # driver_path = GeckoDriverManager().install() # this doesn't work for some reason
        service = Service(driver_path)
        
        self.driver = webdriver.Firefox(service=service, options=options)
        return self.driver

    def connect_to_system(self, username, password):
        if not self.driver:
            self.setup_driver(headless=False)
        self.driver.get("https://kepler-beta.itu.edu.tr/")
        
        if "Tüm İTÜ hizmetleri" in self.driver.page_source:
            username_input = self.driver.find_element(By.ID, "ContentPlaceHolder1_tbUserName")
            password_input = self.driver.find_element(By.ID, "ContentPlaceHolder1_tbPassword")
            login_button = self.driver.find_element(By.ID, "ContentPlaceHolder1_btnLogin")

            username_input.send_keys(username)
            password_input.send_keys(password)
            login_button.click()

            if "Kullanıcı adı veya şifre hatalı." in self.driver.page_source:
                raise Exception("Kullanıcı adı veya şifre hatalı.")

    def find_element_with_timeout(self, by, locator, timeout=3):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((by, locator))
            )
            return element
        except TimeoutException:
            return None

    def close_driver(self):
        if self.driver:
            self.driver.quit()