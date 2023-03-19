
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.setup import WebDriverSetup
from selenium.webdriver.common.by import By

class TestOH(WebDriverSetup):

    def test_53_Sign_up_with_valid_details(self):
        self.sign_up_page.click_sign_up()
        # Enter valid details
        username = self.sign_up_page.forloop_username_valid()
        self.sign_up_page.set_username(username)
        self.sign_up_page.set_password("123")
        self.sign_up_page.click_sign_us_in_pop()
        alert = WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        # Check if a message appears "Sign up successful."
        self.assertEqual(alert.text, "Sign up successful.")

    def test_54_Sign_up_with_exists_user(self):
        self.sign_up_page.click_sign_up()
        # Enter valid details that already exist in the system
        self.sign_up_page.set_username("bdika1")
        self.sign_up_page.set_password("123")
        self.sign_up_page.click_sign_us_in_pop()
        alert = WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        # Check if a message appears "Sign up successful."
        self.assertEqual(alert.text, "This user already exist.")

    def test_55_Sign_up_close(self):
        self.sign_up_page.click_sign_up()
        self.sign_up_page.click_sign_up_close()
        # Check if the Signup popup window closes
        assert self.sign_up_page.Sign_up_pop_up_close()

    def test_56_Sign_up_username_max_10_char(self):
        self.sign_up_page.click_sign_up()
        # Enter valid details, in the username enter more than 10 characters
        username = self.sign_up_page.forloop_username_invalid()
        self.sign_up_page.set_username(username)
        self.sign_up_page.set_password("123")
        self.sign_up_page.click_sign_us_in_pop()
        alert = WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        # Check if a message appears "You need a maximum of 10 characters in the username."
        if len(username) <= 10:
            self.assertEqual(alert.text, "Sign up successful.")
        else:
            self.assertEqual(alert.text, "You need a maximum of 10 characters in the user name.")

    def test_59_send_empty_Sigh_up(self):
        self.sign_up_page.click_sign_up()
        self.sign_up_page.click_sign_us_in_pop()
        alert = WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        # Check if a message appears "Please fill out Username and Password."
        self.assertEqual(alert.text, "Please fill out Username and Password.")
