from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.login_page_locators import LoginLocators

class LoginPage:
    # class attributes
    user_name_text = LoginLocators.user_name_text
    password_text = 'password'
    login_xpath = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'

    def __init__(self, driver):
        self.driver = driver
    def set_username(self, username):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.NAME,self.user_name_text))).send_keys(username)
    def set_password(self, password):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.NAME,self.password_text))).send_keys(password)
    def click_login(self):
        WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.XPATH,self.login_xpath))).click()


