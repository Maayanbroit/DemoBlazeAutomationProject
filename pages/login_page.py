

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.login_locators import LoginLocators

class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def click_log_in_btn(self):
        WebDriverWait(self.driver,10).until(
            EC.visibility_of_element_located((By.XPATH, LoginLocators.login_menu_btn))).click()

    def set_username(self, username):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.ID,LoginLocators.login_username))).send_keys(username)

    def set_password(self, password):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID,LoginLocators.login_password))).send_keys(password)

    def click_login(self):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,LoginLocators.login_btn))).click()

    def login_close_btn(self):
       close_btn = self.driver.find_element(By.XPATH, '//*[@id="logInModal"]/div/div/div[3]/button[1]')
       return close_btn


    def click_logout(self):
         WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, LoginLocators.log_out_btn))).click()

    def logout_not_displayed(self):
        text = WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located((By.XPATH, LoginLocators.log_out_btn)))
        return text



    def welcome_displayed(self):
       welcome = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, LoginLocators.welcome_user_id))).is_displayed()
       return welcome


    def log_in_process(self):
        self.click_log_in_btn()
        self.set_username('Bdika')
        self.set_password('123')
        self.click_login()


