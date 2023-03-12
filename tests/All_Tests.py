import unittest
import random
import string
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
from utilities.driver import get_chrome_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from time import sleep
from pages.home_page import LoginPage
from pages.home_page import Buttons
from pages.home_page import ValidOrder
from pages.home_page import Sign_up
from pages.home_page import Cart
from pages.home_page import Contact
from pages.home_page import Log_in


class TestOH(unittest.TestCase):
    def setUp(self):
        try:
            self.driver = get_chrome_driver()
            self.driver.maximize_window()
            self.driver.get('https://www.demoblaze.com/index.html')
            sleep(3)
        except AssertionError:
            self.driver.quit()

    def tearDown(self):
        # Quit the browser
        self.driver.quit()

    def test_1_valid_text_home_btn(self):
        x = Buttons(self.driver)
        button = x.txt_home_btn()
        button_text = button.text
        self.assertEqual(button_text, "Home")

    def test_2_valid_text_contact_btn(self):
        x = Buttons(self.driver)
        button = x.txt_contact_btn()
        button_text = button.text
        self.assertEqual(button_text, "Contact")

    def test_3_valid_text_about_us_btn(self):
        x = Buttons(self.driver)
        button = x.txt_about_us_btn()
        button_text = button.text
        self.assertEqual(button_text, "About us")

    def test_4_valid_text_cart_btn(self):
        x = Buttons(self.driver)
        button = x.txt_cart_btn()
        button_text = button.text
        self.assertEqual(button_text, "Cart")

    def test_5_valid_text_log_in_btn(self):
        x = Buttons(self.driver)
        button = x.txt_log_in_btn()
        button_text = button.text
        expected_text = 'Log in'
        self.assertEqual(button_text, expected_text)

    def test_6_valid_text_sign_up_btn(self):
        x = Buttons(self.driver)
        button = x.txt_sign_up_btn()
        button_text = button.text
        self.assertEqual(button_text, "Sign up")

    def test_7_click_Home_btn(self):
        x = Buttons(self.driver)
        x.click_home()
        sleep(2)
        assert self.driver.current_url == "https://www.demoblaze.com/index.html"

    def test_8_click_Contact_btn(self):
        c_page = Buttons(self.driver)
        c_page.click_Contact()
        sleep(2)
        assert self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div").is_displayed()

    def test_9_click_About_us_btn(self):
        c_page = Buttons(self.driver)
        c_page.click_About_us()
        sleep(2)
        assert self.driver.find_element(By.XPATH, "/html/body/div[4]/div/div").is_displayed()

    def test_10_click_Cart_bnt(self):
        c_page = Buttons(self.driver)
        c_page.click_Cart()
        sleep(2)
        assert self.driver.current_url == "https://www.demoblaze.com/cart.html"

    def test_11_click_Log_in_btn(self):
        c_page = Buttons(self.driver)
        c_page.click_Login()
        sleep(2)
        assert self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div").is_displayed()

    def test_12_click_Sign_up_btn(self):
        c_page = Buttons(self.driver)
        c_page.click_Sign_up()
        sleep(2)
        assert self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div").is_displayed()

    def test_13_top_logo_redirect_home(self):
        top_logo = Buttons(self.driver)
        top_logo.click_logo()
        sleep(5)
        assert self.driver.current_url == 'https://www.demoblaze.com/index.html'

    def test_14_redirect_to_view_product_page(self):
        product_button = Buttons(self.driver)
        product_button.click_product()
        sleep(3)
        assert self.driver.current_url == 'https://www.demoblaze.com/prod.html?idp_=1'

    def test_15_product_title(self):
        x = Buttons(self.driver)
        external_title = x.txt_product_btn()
        external_title_text = external_title.text
        print(external_title_text)
        external_title.click()
        sleep(3)
        inner_title = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="tbodyid"]/h2')))
        internal_title_text = inner_title.text
        print(internal_title_text)
        sleep(2)
        assert external_title_text == internal_title_text

    def test_16_product_image(self):
        external_image = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="tbodyid"]/div[1]/div/a/img')))
        external_image_src = external_image.get_attribute('src')
        external_image.click()
        inner_image = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="imgp"]/div/img')))
        inner_image_src = inner_image.get_attribute('src')
        sleep(5)
        print(inner_image_src)
        self.assertEqual(external_image_src, inner_image_src)

    def test_17_scroll_down_home_page(self):
        sleep(5)
        scroll = self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(5)
        assert self.driver.execute_script("return window.scrollY") > 0, "Scrolling down the page not working"

    def test_18_valid_text_sign_ip_btn(self):
        external_title = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/div[5]/div/div[2]/div/div[1]/div/div/p')))
        external_title_text = external_title.text
        external_btn = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="tbodyid"]/div[1]/div/div/h4/a')))
        external_btn.click()
        inner_title = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/div[5]/div/div[2]/div[1]/div/div/p')))
        inner_title_text = inner_title.text
        self.assertEqual(external_title_text, inner_title_text)

    def test_19_valid_previous_btn(self):
        left_corn_product = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[5]/div/div[2]/div/div[1]/div/div/h4/a")))
        left_corn_product_text = left_corn_product.text
        prev_btn = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/div[5]/div/div[2]/form/ul/li[1]/button')))
        prev_btn.click()
        sleep(5)
        left_corn_product_after = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/div[5]/div/div[2]/div/div[1]/div/div/h4/a')))
        left_corn_product_after_text = left_corn_product_after.text
        self.assertNotEqual(left_corn_product_text, left_corn_product_after_text)

    def test_20_valid_next_btn(self):
        left_corn_product = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[5]/div/div[2]/div/div[1]/div/div/h4/a")))
        left_corn_product_text = left_corn_product.text
        next_btn = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/div[5]/div/div[2]/form/ul/li[2]/button')))
        next_btn.click()
        sleep(5)
        left_corn_product_after = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/div[5]/div/div[2]/div/div[1]/div/div/h4/a')))
        left_corn_product_after_text = left_corn_product_after.text
        self.assertNotEqual(left_corn_product_text, left_corn_product_after_text)

    def test_21_next_button_displayed_previous_not(self):
        self.scroll = self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(5)
        is_next_btn_display = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, 'next2'))).is_displayed()
        is_previous_btn_display = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, "prev2"))).is_displayed()

        assert is_previous_btn_display == False and is_next_btn_display == True

    def test_22_previous_button_displayed_next_not(self):
        self.scroll = self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(2)
        next_btn = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.ID, 'next2')))
        next_btn.click()
        sleep(2)
        is_next_btn_display = next_btn.is_displayed()
        is_previous_btn_display = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.ID, "prev2"))).is_displayed()

        assert is_previous_btn_display == True and is_next_btn_display == False

    def test_27_image_bar_r_btn(self):
        arrow_btn = Buttons(self.driver)
        self.driver.find_element(By.XPATH, "/html/body/nav/div[2]/div/a[2]").click()
        sleep(1)
        image_1 = self.driver.find_element(By.XPATH, "/html/body/nav/div[2]/div/div/div[1]/img").is_displayed()
        image_2 = self.driver.find_element(By.XPATH, "/html/body/nav/div[2]/div/div/div[2]/img").is_displayed()
        self.assertNotEqual(image_1, image_2)

    def test_28_image_bar_l_btn(self):
        arrow_btn = Buttons(self.driver)
        self.driver.find_element(By.XPATH, "/html/body/nav/div[2]/div/a[1]").click()
        sleep(1)
        image_1 = self.driver.find_element(By.XPATH, "/html/body/nav/div[2]/div/div/div[1]/img").is_displayed()
        image_3 = self.driver.find_element(By.XPATH, "/html/body/nav/div[2]/div/div/div[3]/img").is_displayed()
        self.assertNotEqual(image_1, image_3)

    def test_29_about_as_text(self):
        sleep(5)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(5)
        assert self.driver.find_element(By.XPATH, '/html/body/div[6]/div/div[1]').is_displayed()

    def test_30_get_in_touch_text(self):
        sleep(5)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(5)
        assert self.driver.find_element(By.XPATH, '/html/body/div[6]/div/div[2]').is_displayed()

    def test_31_valid_new_message(self):
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
        new_message = Contact(self.driver)
        new_message.click_contact_btn()
        sleep(3)
        new_message.click_close_btn()
        sleep(2)
        assert WebDriverWait(self.driver, 3).until(EC.invisibility_of_element_located((By.XPATH, "/html/body/div[1]/div/div")))

    def test_34_256_limit(self):
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

    def test_37_send_empty_message(self):
        c_page = Buttons(self.driver)
        c_page.click_Contact()
        c_page.click_send_message()
        sleep(2)
        alert = WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        self.assertEqual(alert.text, "Details not filled in.")

    def test_38_About_us_video(self):
        c_page = Buttons(self.driver)
        c_page.click_About_us()
        sleep(2)
        c_page.click_play_video()
        sleep(2)
        assert self.driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div[2]/form/div/div/video").is_enabled()

    def test_39_About_us_close(self):
        c_page = Buttons(self.driver)
        c_page.click_About_us()
        WebDriverWait(self.driver, 5)
        c_page.click_about_us_close()
        assert WebDriverWait(self.driver, 5).until(EC.invisibility_of_element_located((By.XPATH, "/html/body/div[4]/div/div")))

    def test_40_add_prod_to_cart_valid(self):
        left_corn_product = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[5]/div/div[2]/div/div[1]/div/div/h4/a")))
        left_corn_product_text = left_corn_product.text
        left_corn_product.click()
        sleep(5)
        add_to_cart_btn = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[5]/div/div[2]/div[2]/div/a")))
        add_to_cart_btn.click()
        sleep(5)
        alert = self.driver.switch_to.alert
        alert.accept()
        cart_btn = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/nav/div/div/ul/li[4]/a")))
        cart_btn.click()
        sleep(5)
        title_in_cart = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[6]/div/div[1]/div/table/tbody/tr/td[2]")))
        title_in_cart_text = title_in_cart.text
        self.assertEqual(left_corn_product_text, title_in_cart_text)

    def test_41_add_3times_prod_to_cart_valid(self):
        left_corn_product = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[5]/div/div[2]/div/div[1]/div/div/h4/a")))
        left_corn_product_text = left_corn_product.text
        left_corn_product.click()
        sleep(5)
        add_to_cart_btn = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[5]/div/div[2]/div[2]/div/a")))

        add_to_cart_btn.click()
        sleep(5)
        alert = self.driver.switch_to.alert
        alert.accept()
        add_to_cart_btn.click()
        sleep(5)
        alert = self.driver.switch_to.alert
        alert.accept()
        add_to_cart_btn.click()
        sleep(5)
        alert = self.driver.switch_to.alert
        alert.accept()

        cart_btn = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/nav/div/div/ul/li[4]/a")))
        cart_btn.click()
        sleep(5)
        title_in_cart_1 = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[6]/div/div[1]/div/table/tbody/tr/td[2]")))
        title_in_cart_text_1 = title_in_cart_1.text
        self.assertEqual(left_corn_product_text, title_in_cart_text_1)

        title_in_cart_2 = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[6]/div/div[1]/div/table/tbody/tr[2]/td[2]")))
        title_in_cart_text_2 = title_in_cart_2.text
        self.assertEqual(left_corn_product_text, title_in_cart_text_2)

        title_in_cart_3 = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, "//html/body/div[6]/div/div[1]/div/table/tbody/tr[3]/td[2]")))
        title_in_cart_text_3 = title_in_cart_3.text
        self.assertEqual(left_corn_product_text, title_in_cart_text_3)

    def test_42_prod_add_popup_valid(self):
        left_corn_product = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[5]/div/div[2]/div/div[1]/div/div/h4/a")))
        left_corn_product.click()
        sleep(5)
        add_to_cart_btn = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[5]/div/div[2]/div[2]/div/a")))
        add_to_cart_btn.click()
        alert = WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        self.assertEqual(alert.text, "Product added")
        sleep(5)
        alert = self.driver.switch_to.alert
        alert.accept()

    def test_43_prod_price_valid(self):
        left_corn_product = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[5]/div/div[2]/div/div[1]/div/div/h4/a")))
        left_corn_product_price = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[5]/div/div[2]/div/div[1]/div/div/h5")))
        left_corn_product_price = left_corn_product_price.text
        left_corn_product.click()
        sleep(5)
        add_to_cart_btn = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[5]/div/div[2]/div[2]/div/a")))
        add_to_cart_btn.click()
        sleep(5)
        alert = self.driver.switch_to.alert
        alert.accept()
        cart_btn = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/nav/div/div/ul/li[4]/a")))
        cart_btn.click()
        sleep(5)
        price_in_cart = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[6]/div/div[1]/div/table/tbody/tr/td[3]")))
        price_in_cart = price_in_cart.text
        self.assertEqual(price_in_cart, left_corn_product_price)

    def test_44_del_prod_from_cart_valid(self):
        left_corn_product = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[5]/div/div[2]/div/div[1]/div/div/h4/a")))
        left_corn_product_text = left_corn_product.text
        left_corn_product.click()
        sleep(5)
        add_to_cart_btn = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[5]/div/div[2]/div[2]/div/a")))
        add_to_cart_btn.click()
        sleep(5)
        alert = self.driver.switch_to.alert
        alert.accept()
        cart_btn = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/nav/div/div/ul/li[4]/a")))
        cart_btn.click()
        sleep(5)
        title_in_cart = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[6]/div/div[1]/div/table/tbody/tr/td[2]")))
        title_in_cart_text = title_in_cart.text
        self.assertEqual(left_corn_product_text, title_in_cart_text)
        delete_btn = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[6]/div/div[1]/div/table/tbody/tr/td[4]/a")))
        delete_btn.click()
        sleep(5)
        title_in_cart = WebDriverWait(self.driver, 5).until(
            EC.invisibility_of_element_located((By.XPATH, "/html/body/div[6]/div/div[1]/div/table/tbody/tr/td[2]")))
        assert title_in_cart

    def test_45_delete_details(self):
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
        x = Buttons(self.driver)
        y = Cart(self.driver)
        x.click_Cart()
        sleep(5)
        y.click_place_order_btn()
        sleep(5)
        element = WebDriverWait(self.driver, 5).until(
            EC.invisibility_of_element_located((By.XPATH, "/html/body/div[3]/div/div")))
        assert element

    def test_47_valid_order_without_login(self):
        valid_order = ValidOrder(self.driver)
        product_button = Buttons(self.driver)
        product_button.click_product()
        product_button.click_add_cart()
        alert = WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        alert.accept()
        product_button.click_cart()
        product_button.click_place_order()
        valid_order.fill_name('Shiran')
        valid_order.fill_country('Israel')
        valid_order.fill_city('Kfar Yona')
        valid_order.fill_card('552211')
        valid_order.fill_month('5')
        valid_order.fill_year('2030')
        product_button.click_purchase()
        sleep(5)
        assert self.driver.find_element(By.XPATH, '/html/body/div[9]').is_displayed()

    def test_48_purchase_button_disable(self):
        valid_order = ValidOrder(self.driver)
        buttons = Buttons(self.driver)
        buttons.click_product()
        buttons.click_add_cart()
        alert = WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        alert.accept()
        buttons.click_cart()
        buttons.click_place_order()
        valid_order.fill_name('Shiran')
        valid_order.fill_country('Israel')
        valid_order.fill_city('Kfar Yona')
        valid_order.fill_card('552211')
        valid_order.fill_month('5')
        valid_order.fill_year('2030')
        buttons.click_purchase()
        sleep(2)
        is_purchase_btn_enabled = buttons.check_is_purchase_btn_enabled()
        print(is_purchase_btn_enabled)
        assert is_purchase_btn_enabled == False

    def test_49_empty_order_without_login(self):
        valid_order = ValidOrder(self.driver)
        product_button = Buttons(self.driver)
        product_button.click_cart()
        product_button.click_place_order()
        valid_order.fill_name('Shiran')
        valid_order.fill_country('Israel')
        valid_order.fill_city('Kfar Yona')
        valid_order.fill_card('552211')
        valid_order.fill_month('5')
        valid_order.fill_year('2030')
        product_button.click_purchase()
        sleep(5)
        assert WebDriverWait(self.driver, 5).until(EC.invisibility_of_element_located((By.XPATH, '/html/body/div[9]')))

    def test_50_valid_order_with_login(self):
        self.driver.maximize_window()
        self.driver.get('https://www.demoblaze.com/index.html')
        valid_order = ValidOrder(self.driver)
        product_button = Buttons(self.driver)
        lp = LoginPage(self.driver)
        product_button.click_login_btn()
        lp.set_username('Bdika')
        lp.set_password('123')
        lp.click_login()
        sleep(3)
        product_button.click_product()
        sleep(3)
        product_button.click_add_cart()
        alert = WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        alert.accept()
        product_button.click_cart()
        product_button.click_place_order()
        valid_order.fill_name('Shiran')
        valid_order.fill_country('Israel')
        valid_order.fill_city('Kfar Yona')
        valid_order.fill_card('552211')
        valid_order.fill_month('5')
        valid_order.fill_year('2030')
        product_button.click_purchase()
        sleep(5)

        assert self.driver.find_element(By.XPATH, '/html/body/div[9]').is_displayed()

    def test_51_empty_order_with_login(self):
        self.driver.maximize_window()
        self.driver.get('https://www.demoblaze.com/index.html')
        valid_order = ValidOrder(self.driver)
        product_button = Buttons(self.driver)
        lp = LoginPage(self.driver)
        product_button.click_login_btn()
        lp.set_username('Bdika')
        lp.set_password('123')
        lp.click_login()
        sleep(3)
        product_button.click_cart()
        product_button.click_place_order()
        valid_order.fill_name('Shiran')
        valid_order.fill_country('Israel')
        valid_order.fill_city('Kfar Yona')
        valid_order.fill_card('552211')
        valid_order.fill_month('5')
        valid_order.fill_year('2030')
        product_button.click_purchase()
        sleep(5)
        assert WebDriverWait(self.driver, 5).until(EC.invisibility_of_element_located((By.XPATH, '/html/body/div[9]')))

    def test_53_Sign_up_with_valid_details(self):
        c_page = Buttons(self.driver)
        c_page.click_Sign_up()
        WebDriverWait(self.driver, 5)
        c_page1 = Sign_up(self.driver)

        str1 = ""
        for i in range(6):
            x = random.choice(string.ascii_letters)
            str1 = str1 + x

        c_page1.set_username(str1)
        WebDriverWait(self.driver, 5)
        c_page1.set_password("123")
        WebDriverWait(self.driver, 5)
        c_page1.click_sign_us_in_pop()
        sleep(2)
        alert = WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        self.assertEqual(alert.text, "Sign up successful.")

    def test_54_Sign_up_with_exists_user(self):
        c_page = Buttons(self.driver)
        c_page.click_Sign_up()
        WebDriverWait(self.driver, 5)
        c2_page = Sign_up(self.driver)
        c2_page.set_username("bdika1")
        WebDriverWait(self.driver, 5)
        c2_page.set_password("123")
        WebDriverWait(self.driver, 5)
        c2_page.click_sign_us_in_pop()
        sleep(2)
        alert = WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        self.assertEqual(alert.text, "This user already exist.")

    def test_55_Sign_up_close(self):
        c_page = Buttons(self.driver)
        c_page.click_Sign_up()
        WebDriverWait(self.driver, 5)
        c_page.click_sign_up_close()
        sleep(2)
        assert WebDriverWait(self.driver, 5).until(
            EC.invisibility_of_element_located((By.XPATH, "/html/body/div[2]/div/div")))

    def test_56_Sign_up_username_max_10_char(self):
        c_page = Buttons(self.driver)
        c_page.click_Sign_up()
        WebDriverWait(self.driver, 5)
        c_page1 = Sign_up(self.driver)

        str1 = ""
        for i in range(11):
            x = random.choice(string.ascii_letters)
            str1 = str1 + x

        username = c_page1.set_username(str1)
        WebDriverWait(self.driver, 5)
        c_page1.set_password("123")
        WebDriverWait(self.driver, 5)
        c_page1.click_sign_us_in_pop()
        sleep(2)
        alert = WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        if len(username) <= 10:
            self.assertEqual(alert.text, "Sign up successful.")
        else:
            self.assertEqual(alert.text, "You need a maximum of 10 characters in the user name.")

    def test_59_send_empty_Sigh_up(self):
        c_page = Buttons(self.driver)
        c_page.click_signup()
        WebDriverWait(self.driver, 5)
        c_page1 = Sign_up(self.driver)
        c_page1.click_sign_us_in_pop()
        sleep(2)
        alert = WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        self.assertEqual(alert.text, "Please fill out Username and Password.")

    def test_60_Log_in_valid(self):
        lp = Log_in(self.driver)
        lp.click_log_in_btn()
        lp.set_username('tami4')
        lp.set_password('tami4')
        lp.click_login()
        sleep(5)
        assert self.driver.find_element(By.XPATH, '/html/body/nav/div[1]/ul/li[7]/a').is_displayed()

    def test_61_Log_in_invalid(self):
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

    def test_64_login_close_button(self):
        product_button = Buttons(self.driver)
        lp = LoginPage(self.driver)
        product_button.click_login_btn()
        lp.click_close_login()
        sleep(3)
        assert WebDriverWait(self.driver, 5).until(EC.invisibility_of_element_located((By.XPATH, '//*[@id="logInModal"]/div/div')))

    def test_67_login_without_details(self):
        product_button = Buttons(self.driver)
        lp = LoginPage(self.driver)
        product_button.click_login_btn()
        lp.click_login()
        sleep(2)
        alert = Alert(self.driver)
        alert_text = alert.text
        expected_text = "Please fill out Username and Password."
        sleep(2)
        alert.accept()
        self.assertEqual(alert_text, expected_text)


if __name__ == '__main__':
    unittest.main()
