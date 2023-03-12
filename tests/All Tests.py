import unittest
import random
import string
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
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
        self.assertEqual(len(title_in_cart), 0)

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
