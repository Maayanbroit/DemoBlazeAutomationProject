

from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.setup import WebDriverSetup
from selenium.webdriver.common.by import By
from time import sleep



class TestOH(WebDriverSetup):

    def test_60_Log_in_valid(self):
        # Click the log in menu button
        self.login_page.click_log_in_btn()
        # Enter a valid username
        self.login_page.set_username('tami4')
        # Enter a valid password
        self.login_page.set_password('tami4')
        # Click log in button
        self.login_page.click_login()
        assert self.login_page.welcome_displayed()


    def test_61_Log_in_invalid(self):
         # Click the log in menu button
         self.login_page.click_log_in_btn()
         # Enter aa invalid username
         self.login_page.set_username('sunday')
         # Enter an invalid password
         self.login_page.set_password('test')
         # Click the log in button
         self.login_page.click_login()
         # Alert is displayed
         alert = WebDriverWait(self.driver, 5).until(EC.alert_is_present())
         self.assertEqual(alert.text, "User does not exist.")

    def test_62_Log_in_invalid_p(self):
        # Click the log in menu button
        self.login_page.click_log_in_btn()
        # Enter a valid username
        self.login_page.set_username('tami4')
        # Enter an invalid password
        self.login_page.set_password('1234')
        # Click the log in button
        self.login_page.click_login()
        # Alert is displayed
        alert = WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        self.assertEqual(alert.text, "Wrong password.")

    def test_63_Log_out(self):
        # Click the log in menu button
        self.login_page.click_log_in_btn()
        # Enter a valid username
        self.login_page.set_username('tami4')
        # Enter a valid password
        self.login_page.set_password('tami4')
        # Click the log in button
        self.login_page.click_login()
        sleep(3)
        # Click the logout button
        self.login_page.click_logout()
        assert self.login_page.logout_not_displayed()

    def test_64_login_close_button(self):
        self.login_page.click_log_in_btn()
        sleep(2)
        close_btn = self.login_page.login_close_btn()
        close_btn.click()
        sleep(2)
        assert close_btn.is_displayed() == False

    def test_67_login_without_details(self):
        self.login_page.click_log_in_btn()
        self.login_page.click_login()
        alert = Alert(self.driver)
        alert_text = alert.text
        expected_text = "Please fill out Username and Password."
        alert.accept()
        self.assertEqual(alert_text, expected_text)



