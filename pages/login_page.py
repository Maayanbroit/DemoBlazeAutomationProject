

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators1.login_locators import LoginLocators

class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def click_log_in_btn(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, LoginLocators.login_menu_btn))).click()

    def set_username(self, username):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID,LoginLocators.login_username))).send_keys(username)

    def set_password(self, password):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID,LoginLocators.login_password))).send_keys(password)

    def click_login(self):
        WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.XPATH,LoginLocators.login_btn))).click()

    def click_close_login(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, LoginLocators.login_close_xpath))).click()

    def click_logout(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH,LoginLocators.Log_out_btn))).click()

    def log_in_process(self):
        self.click_log_in_btn()
        self.set_username('Bdika')
        self.set_password('123')
        self.click_login()


