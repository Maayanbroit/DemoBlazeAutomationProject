

from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.setup import WebDriverSetup
from selenium.webdriver.common.by import By
from time import sleep



class TestOH(WebDriverSetup):

    def test_60_Log_in_valid(self):
        self.login_page.click_log_in_btn()
        self.login_page.set_username('tami4')
        self.login_page.set_password('tami4')
        self.login_page.click_login()
        element = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, "nameofuser")))
        self.assertTrue(element)


    def test_61_Log_in_invalid(self):
         self.login_page.click_log_in_btn()
         sleep(5)
         self.login_page.set_username('sunday')
         self.login_page.set_password('test')
         self.login_page.click_login()
         sleep(5)
         alert = WebDriverWait(self.driver, 5).until(EC.alert_is_present())
         self.assertEqual(alert.text, "User does not exist.")

    def test_62_Log_in_invalid_p(self):
        self.login_page.click_log_in_btn()
        sleep(5)
        self.login_page.set_username('tami4')
        self.login_page.set_password('1234')
        self.login_page.click_login()
        sleep(5)
        alert = WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        self.assertEqual(alert.text, "Wrong password.")

    def test_63_Log_out(self):
        self.login_page.click_log_in_btn()
        sleep(5)
        self.login_page.set_username('tami4')
        self.login_page.set_password('tami4')
        self.login_page.click_login()
        sleep(5)
        self.login_page.click_logout()
        sleep(5)
        assert not self.driver.find_element(By.XPATH, '/html/body/nav/div[1]/ul/li[6]/a').is_displayed()

    def test_64_login_close_button(self):
        self.login_page.click_log_in_btn()
        self.login_page.click_close_login()
        assert WebDriverWait(self.driver, 5).until(EC.invisibility_of_element_located((By.XPATH, '//*[@id="logInModal"]/div/div')))

    def test_67_login_without_details(self):
        self.login_page.click_log_in_btn()
        self.login_page.click_login()
        alert = Alert(self.driver)
        alert_text = alert.text
        expected_text = "Please fill out Username and Password."
        alert.accept()
        self.assertEqual(alert_text, expected_text)



