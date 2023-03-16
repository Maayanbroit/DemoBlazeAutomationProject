
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.setup import WebDriverSetup
from selenium.webdriver.common.by import By
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
        assert WebDriverWait(self.driver, 3).until(EC.invisibility_of_element_located((By.XPATH, "/html/body/div[1]/div/div")))

    def test_34_256_limit(self):
        # Click the contact button
        self.contact_page.click_contact_btn()
        # Enter a valid email
        self.contact_page.set_email('test@gmail.com')
        # Enter a valid name
        self.contact_page.set_name('maya')
        # Enter invalid message more then 256
        x = self.contact_page.set_message("1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256,1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 110, 211, 412, 213, 214, 815, 216, 717, 418, 219, 220, 221, 222, 223, 824, 925, 226, 327, 228, 529, 630, 231, 232, 233, 234, 235, 336, 437, 238, 239, 640, 941, 842, 743, 944, 845, 746, 647, 548, 549, 550, 451, 352, 353, 354, 355, 356,")
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
