import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from utilities.driver import get_chrome_driver
from pages.home_page import LoginPage

from pages.home_page import Buttons
from pages.home_page import ValidOrder
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestDemoBlaze(unittest.TestCase):
    def setUp(self):
        try:
            self.driver = get_chrome_driver()
        except AssertionError:
            self.driver.quit()

    def tearDown(self):
        # Quit the browser
        self.driver.quit()


    def test_13_top_logo_redirect_home(self):
        self.driver.maximize_window()
        self.driver.get('https://www.demoblaze.com/index.html')
        top_logo = Buttons(self.driver)
        top_logo.click_logo()
        sleep(5)
        assert self.driver.current_url == 'https://www.demoblaze.com/index.html'


    def test_14_redirect_to_view_product_page(self):
        self.driver.maximize_window()
        self.driver.get('https://www.demoblaze.com/index.html')
        product_button = Buttons(self.driver)
        product_button.click_product()
        sleep(3)
        assert self.driver.current_url == 'https://www.demoblaze.com/prod.html?idp_=1'



    def test_15_product_title(self):
        self.driver.maximize_window()
        self.driver.get('https://www.demoblaze.com/index.html')
        external_title = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="tbodyid"]/div[1]/div/div/h4/a')))
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
        self.driver.maximize_window()
        self.driver.get('https://www.demoblaze.com/index.html')
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
        self.driver.maximize_window()
        self.driver.get('https://www.demoblaze.com/index.html')
        sleep(5)
        scroll = self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(5)
        assert self.driver.execute_script("return window.scrollY") > 0, "Scrolling down the page not working"


    def test_21_next_button_displayed_previous_not(self):
        self.driver.maximize_window()
        self.driver.get('https://www.demoblaze.com/index.html')
        sleep(5)
        self.scroll = self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(5)
        is_next_btn_display = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, 'next2'))).is_displayed()
        is_previous_btn_display = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, "prev2"))).is_displayed()

        assert is_previous_btn_display == False and is_next_btn_display == True


    def test_22_previous_button_displayed_next_not(self):
        self.driver.maximize_window()
        self.driver.get('https://www.demoblaze.com/index.html')
        sleep(5)
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


    def test_47_valid_order_without_login(self):
        self.driver.maximize_window()
        self.driver.get('https://www.demoblaze.com/index.html')
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
        self.driver.maximize_window()
        self.driver.get('https://www.demoblaze.com/index.html')
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
        self.driver.maximize_window()
        self.driver.get('https://www.demoblaze.com/index.html')
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




    def test_64_login_close_button(self):
        self.driver.maximize_window()
        self.driver.get('https://www.demoblaze.com/index.html')
        product_button = Buttons(self.driver)
        lp = LoginPage(self.driver)
        product_button.click_login_btn()
        lp.click_close_login()
        sleep(3)
        assert WebDriverWait(self.driver, 5).until(EC.invisibility_of_element_located((By.XPATH, '//*[@id="logInModal"]/div/div')))



    def test_67_login_without_details(self):
        self.driver.maximize_window()
        self.driver.get('https://www.demoblaze.com/index.html')
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



























