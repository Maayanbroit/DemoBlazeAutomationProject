
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.setup import WebDriverSetup
from selenium.webdriver.common.by import By
from time import sleep
import random
import string


class TestOH(WebDriverSetup):

    def test_53_Sign_up_with_valid_details(self):
        self.sign_up_page.click_sign_up()
        WebDriverWait(self.driver, 5)

        str1 = ""
        for i in range(6):
            x = random.choice(string.ascii_letters)
            str1 = str1 + x

        self.sign_up_page.set_username(str1)
        WebDriverWait(self.driver, 5)
        self.sign_up_page.set_password("123")
        WebDriverWait(self.driver, 5)
        self.sign_up_page.click_sign_us_in_pop()
        sleep(2)
        alert = WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        self.assertEqual(alert.text, "Sign up successful.")

    def test_54_Sign_up_with_exists_user(self):
        self.sign_up_page.click_sign_up()
        WebDriverWait(self.driver, 5)
        self.sign_up_page.set_username("bdika1")
        WebDriverWait(self.driver, 5)
        self.sign_up_page.set_password("123")
        WebDriverWait(self.driver, 5)
        self.sign_up_page.click_sign_us_in_pop()
        sleep(2)
        alert = WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        self.assertEqual(alert.text, "This user already exist.")

    def test_55_Sign_up_close(self):
        self.sign_up_page.click_sign_up()
        WebDriverWait(self.driver, 5)
        self.sign_up_page.click_sign_up_close()
        sleep(2)
        assert WebDriverWait(self.driver, 5).until(
            EC.invisibility_of_element_located((By.XPATH, "/html/body/div[2]/div/div")))

    def test_56_Sign_up_username_max_10_char(self):
        self.sign_up_page.click_sign_up()
        WebDriverWait(self.driver, 5)

        str1 = ""
        for i in range(11):
            x = random.choice(string.ascii_letters)
            str1 = str1 + x

        username = self.sign_up_page.set_username(str1)
        WebDriverWait(self.driver, 5)
        self.sign_up_page.set_password("123")
        WebDriverWait(self.driver, 5)
        self.sign_up_page.click_sign_us_in_pop()
        sleep(2)
        alert = WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        if len(username) <= 10:
            self.assertEqual(alert.text, "Sign up successful.")
        else:
            self.assertEqual(alert.text, "You need a maximum of 10 characters in the user name.")

    def test_59_send_empty_Sigh_up(self):
        self.sign_up_page.click_sign_up()
        WebDriverWait(self.driver, 5)
        self.sign_up_page.click_sign_us_in_pop()
        sleep(2)
        alert = WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        self.assertEqual(alert.text, "Please fill out Username and Password.")
