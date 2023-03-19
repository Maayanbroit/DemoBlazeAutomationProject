
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.setup import WebDriverSetup
from selenium.webdriver.common.by import By
from locators.contact_locators import ContactLocators
from time import sleep


class TestOH(WebDriverSetup):


    def test_31_valid_new_message(self):
        # Click the contact button
        self.contact_page.click_contact_btn()
        # Enter a valid email
        self.contact_page.set_email('test@gmail.com')
        # Enter a valid name
        self.contact_page.set_name('maya')
        # Enter a valid message
        self.contact_page.set_message("hello, how are you?")
        # Click the send message button
        self.contact_page.click_send_message()
        # Alert is displayed
        alert = WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        self.assertEqual(alert.text, "Thanks for the message!!")

    def test_32_ivalid_new_message(self):
        # Click the contact button
        self.contact_page.click_contact_btn()
        # Enter an invalid email
        self.contact_page.set_email('test///gmail.com')
        # Enter a valid name
        self.contact_page.set_name('maya')
        # Enter a valid message
        self.contact_page.set_message("hello, what is your name?")
        # Click the send message button
        self.contact_page.click_send_message()
        # Alert is displayed
        alert = WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        self.assertEqual(alert.text, "the email is incorrect.")

    def test_33_close_btn_new_message(self):
        # Click the contact button
        self.contact_page.click_contact_btn()
        # Click the close contact button
        self.contact_page.click_close_btn()
        assert self.contact_page.contact_popup_not_displayed()
        # assert WebDriverWait(self.driver, 3).until(EC.invisibility_of_element_located((By.XPATH, ContactLocators.close_new_message_btn)))

    def test_34_256_limit(self):
        # Click the contact button
        self.contact_page.click_contact_btn()
        # Enter a valid email
        self.contact_page.set_email('test@gmail.com')
        # Enter a valid name
        self.contact_page.set_name('maya')
        # Enter invalid message more then 256
        x = self.contact_page.forloop_message_invalid()
        # Click the send message button
        self.contact_page.click_send_message()
        # Alert is displayed
        alert = WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        if len(x) <= 256:
            self.assertEqual(alert.text, "Thank you for the message!!")
        else:
            self.assertEqual(alert.text, "you need a maximum of 256 characters in the message.")

    def test_37_send_empty_message(self):
        self.contact_page.click_contact_btn()
        self.contact_page.click_send_message()
        alert = WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        # Check if a message appears "Details not filled in."
        self.assertEqual(alert.text, "Details not filled in.")
