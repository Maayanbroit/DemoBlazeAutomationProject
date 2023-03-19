
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.sign_up_locators import Sign_Up_Locators
import random
import string

class Sign_Up_Page:


        def __init__(self, driver):
            self.driver = driver

        def click_sign_up(self):
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, Sign_Up_Locators.sign_up_btn))).click()
            WebDriverWait(self.driver, 5)

        def set_username(self, username):
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.ID, Sign_Up_Locators.user_name_text))).send_keys(
                username)
            #return username

        def set_password(self, password):
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.ID, Sign_Up_Locators.password_text))).send_keys(
                password)

        def click_sign_us_in_pop(self):
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, Sign_Up_Locators.sign_up_xpath))).click()
            WebDriverWait(self.driver, 5)
        def click_sign_up_close(self):
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, Sign_Up_Locators.sign_up_close_btn))).click()
        def forloop_username_valid(self):
            str1 = ""
            for i in range(6):
                x = random.choice(string.ascii_letters)
                str1 = str1 + x
            return str1

        def forloop_username_invalid(self):
            str1 = ""
            for i in range(11):
                x = random.choice(string.ascii_letters)
                str1 = str1 + x
            return str1

        #assert test 55:
        def Sign_up_pop_up_close(self):
            x = WebDriverWait(self.driver, 5).until(
            EC.invisibility_of_element_located((By.XPATH, Sign_Up_Locators.Sign_up_pop_up)))
            return x