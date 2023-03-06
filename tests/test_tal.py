from time import sleep
import unittest
from utilities.driver import get_chrome_driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.home_page import Buttons
from pages.home_page import Log_in
from pages.home_page import Contact
from pages.home_page import Cart
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys





class TestOH(unittest.TestCase):
    def setUp(self):
        try:
            self.driver = get_chrome_driver()
        except AssertionError:
            self.driver.quit()

    def tearDown(self):
        # Quit the browser
        self.driver.quit()

    def test_27_image_bar_r_btn(self):
        self.driver.maximize_window()
        self.driver.get("https://www.demoblaze.com/index.html")
        arrow_btn = Buttons(self.driver)
        self.driver.find_element(By.XPATH, "/html/body/nav/div[2]/div/a[2]").click()
        sleep(1)
        image_1 = self.driver.find_element(By.XPATH, "/html/body/nav/div[2]/div/div/div[1]/img").is_displayed()
        image_2 = self.driver.find_element(By.XPATH, "/html/body/nav/div[2]/div/div/div[2]/img").is_displayed()
        self.assertNotEqual(image_1, image_2)


    def test_28_image_bar_l_btn(self):
        self.driver.maximize_window()
        self.driver.get("https://www.demoblaze.com/index.html")
        arrow_btn = Buttons(self.driver)
        self.driver.find_element(By.XPATH, "/html/body/nav/div[2]/div/a[1]").click()
        sleep(1)
        image_1 = self.driver.find_element(By.XPATH, "/html/body/nav/div[2]/div/div/div[1]/img").is_displayed()
        image_3 = self.driver.find_element(By.XPATH, "/html/body/nav/div[2]/div/div/div[3]/img").is_displayed()
        self.assertNotEqual(image_1, image_3)




    def test_29_about_as_text(self):
        self.driver.maximize_window()
        self.driver.get("https://www.demoblaze.com/index.html")
        sleep(5)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(5)
        assert self.driver.find_element(By.XPATH, '/html/body/div[6]/div/div[1]').is_displayed()

    def test_30_get_in_touch_text(self):
        self.driver.maximize_window()
        self.driver.get("https://www.demoblaze.com/index.html")
        sleep(5)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(5)
        assert self.driver.find_element(By.XPATH, '/html/body/div[6]/div/div[2]').is_displayed()

    def test_31_valid_new_message(self):
        self.driver.maximize_window()
        self.driver.get("https://www.demoblaze.com/index.html")
        new_message = Contact(self.driver)
        new_message.click_contact_btn()
        sleep(3)
        new_message.set_email('test@gmail.com')
        sleep(3)
        new_message.set_name('maya')
        sleep(3)
        new_message.set_message("hello, how are you?")
        new_message.click_send_message()
        alert = WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        sleep(2)
        self.assertEqual(alert.text, "Thanks for the message!!")



    def test_32_ivalid_new_message(self):
        self.driver.maximize_window()
        self.driver.get("https://www.demoblaze.com/index.html")
        new_message = Contact(self.driver)
        new_message.click_contact_btn()
        sleep(5)
        new_message.set_email('test///gmail.com')
        sleep(5)
        new_message.set_name('maya')
        sleep(5)
        new_message.set_message("hello, what is your name?")
        new_message.click_send_message()
        alert = WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        sleep(5)
        self.assertEqual(alert.text, "the email is incorrect.")


    def test_33_close_btn_new_message(self):
        self.driver.maximize_window()
        self.driver.get("https://www.demoblaze.com/index.html")
        new_message = Contact(self.driver)
        new_message.click_contact_btn()
        sleep(3)
        new_message.click_close_btn()
        sleep(2)
        assert WebDriverWait(self.driver, 3).until(EC.invisibility_of_element_located((By.XPATH, "/html/body/div[1]/div/div")))


    def test_34_256_limit(self):
        self.driver.maximize_window()
        self.driver.get("https://www.demoblaze.com/index.html")
        new_message = Contact(self.driver)
        new_message.click_contact_btn()
        sleep(5)
        new_message.set_email('test@gmail.com')
        sleep(5)
        new_message.set_name('maya')
        sleep(5)
        # enter invalid message more then 256
        x = new_message.set_message("1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256,1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 110, 211, 412, 213, 214, 815, 216, 717, 418, 219, 220, 221, 222, 223, 824, 925, 226, 327, 228, 529, 630, 231, 232, 233, 234, 235, 336, 437, 238, 239, 640, 941, 842, 743, 944, 845, 746, 647, 548, 549, 550, 451, 352, 353, 354, 355, 356,")
        new_message.click_send_message()
        alert = WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        if len(x) <= 256:
            self.assertEqual(alert.text, "Thank you for the message!!")
        else:
            self.assertEqual(alert.text, "you need a meximum of 256 characters in the message.")


    def test_45_delete_details(self):
        self.driver.maximize_window()
        self.driver.get("https://www.demoblaze.com/index.html")
        sleep(5)
        add_prodact = Cart(self.driver)
        add_prodact.click_samsung_6s()
        add_prodact.click_add_btn()
        sleep(5)
        alert = WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        alert.accept()
        add_prodact.click_cart_btn()
        sleep(5)
        add_prodact.click_delete_btn()
        sleep(5)
        # assert self.driver.find_element(By.XPATH, '/html/body/div[6]').is_displayed()
        assert self.driver.find_element(By.XPATH, '/html/body/div[6]/div/div[2]').is_displayed()

    def test_46_place_order(self):
        self.driver.maximize_window()
        self.driver.get("https://www.demoblaze.com/index.html")
        order = Cart(self.driver)
        order.click_cart_btn()
        sleep(3)
        order.click_place_order_btn()
        sleep(3)
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(By.TAG_NAME, 'body')).perform()
        action.key_down(Keys.CONTROL).send_keys(Keys.END).key_up(Keys.CONTROL).perform()
        sleep(5)
        assert self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div').is_displayed()


    def test_60_Log_in_valid(self):
        self.driver.maximize_window()
        self.driver.get("https://www.demoblaze.com/index.html")
        lp = Log_in(self.driver)
        lp.click_log_in_btn()
        lp.set_username('tami4')
        lp.set_password('tami4')
        lp.click_login()
        sleep(5)
        assert self.driver.find_element(By.XPATH, '/html/body/nav/div[1]/ul/li[7]/a').is_displayed()


    def test_61_Log_in_invalid(self):
         self.driver.maximize_window()
         self.driver.get("https://www.demoblaze.com/index.html")
         lp = Log_in(self.driver)
         lp.click_log_in_btn()
         sleep(5)
         lp.set_username('sunday')
         lp.set_password('test')
         lp.click_login()
         sleep(5)
         alert = WebDriverWait(self.driver, 5).until(EC.alert_is_present())
         self.assertEqual(alert.text, "User does not exist.")


    def test_62_Log_in_invalid_p(self):
        self.driver.maximize_window()
        self.driver.get("https://www.demoblaze.com/index.html")
        lp = Log_in(self.driver)
        lp.click_log_in_btn()
        sleep(5)
        lp.set_username('tami4')
        lp.set_password('1234')
        lp.click_login()
        sleep(5)
        alert = WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        self.assertEqual(alert.text, "Wrong password.")


    def test_63_Log_out(self):
        self.driver.maximize_window()
        self.driver.get("https://www.demoblaze.com/index.html")
        lp = Log_in(self.driver)
        lp.click_log_in_btn()
        sleep(5)
        lp.set_username('tami4')
        lp.set_password('tami4')
        lp.click_login()
        sleep(5)
        lp.click_logout()
        sleep(5)
        assert not self.driver.find_element(By.XPATH, '/html/body/nav/div[1]/ul/li[6]/a').is_displayed()


if __name__ == '__main__':
    unittest.main()
