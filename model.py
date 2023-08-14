from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options

class Model:
    def __init__(self):
        self.driver = None
        self.course_letter_grades = []
        self.course_credits = []
        self.letter_grade_dict = {"AA": 4.0, "BA": 3.5, "BB": 3.0, "CB": 2.5, "CC": 2.0, "DC": 1.5, "DD": 1.0, "FF": 0.0, "VF": 0.0, "BL": 0.0, "BZ": 0.0}

    def calculate_gpa(self):
        index = 0
        total = 0.0
        for x in self.course_letter_grades:
            total += self.letter_grade_dict[x] * float(self.course_credits[index])
            index += 1
        return total / sum(self.course_credits)
    
    def connect_to_system(self, username, password, pin):
        try:
            edge_options = Options()
            edge_options.add_argument("--headless")
            self.driver = webdriver.Edge(options=edge_options)
            self.driver.get("http://uzay.sis.itu.edu.tr/login/index.php")

            page_content = self.driver.page_source

            if "Tüm İTÜ hizmetleri" in page_content:
                username_input = self.driver.find_element("id", "ContentPlaceHolder1_tbUserName")
                password_input = self.driver.find_element("id", "ContentPlaceHolder1_tbPassword")
                login_button = self.driver.find_element("id", "ContentPlaceHolder1_btnLogin")
                
                username_input.send_keys(username)
                password_input.send_keys(password)
                login_button.click()

                page_content = self.driver.page_source
                
                if "Kullanıcı adı veya şifre hatalı." in page_content:
                    self.driver.close()
                    return "Kullanıcı adı ya da şifre hatalı."
                else:
                    page_content_before = self.driver.page_source

                    pin_input = self.driver.find_element("name", "PIN")
                    pin_input.send_keys(pin)
                    login_obs = self.driver.find_element(By.XPATH, "/html/body/div[3]/form/p/input[1]")
                    login_obs.click()

                    page_content_after = self.driver.page_source
                    
                    if page_content_before == page_content_after:
                        self.driver.close()
                        return "Pin hatalı."
                    else:
                        ogrenci_servisi = self.driver.find_element(By.XPATH, "/html/body/div[3]/table[2]/tbody/tr[1]/td[2]/a")
                        ogrenci_servisi.click()
                        ogrenci_bilgileri = self.driver.find_element(By.XPATH, "/html/body/div[3]/table[1]/tbody/tr[2]/td[2]/a")
                        ogrenci_bilgileri.click()
                        transkript = self.driver.find_element(By.XPATH, "/html/body/div[3]/table[1]/tbody/tr[3]/td[2]/a")
                        transkript.click()
                        return ""
        except:
            self.driver.close()
            return "İTÜ ÖBS'ne ulaşılamadı."
        
    
