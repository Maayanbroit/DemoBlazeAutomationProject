
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators1.sign_up_locators import Sign_Up_Locators

class Sign_Up_Page:


        def __init__(self, driver):
            self.driver = driver

        def click_sign_up(self):
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, Sign_Up_Locators.sign_up_btn))).click()

        def set_username(self, username):
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.ID, Sign_Up_Locators.user_name_text))).send_keys(
                username)
            return username

        def set_password(self, password):
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.ID, Sign_Up_Locators.password_text))).send_keys(
                password)

        def click_sign_us_in_pop(self):
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, Sign_Up_Locators.sign_up_xpath))).click()

        def click_sign_up_close(self):
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, Sign_Up_Locators.sign_up_close_btn))).click()

