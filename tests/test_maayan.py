import unittest
from utilities.driver import get_chrome_driver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

class TestOH(unittest.TestCase):
    def setUp(self):
        try:
            self.driver = get_chrome_driver()
        except AssertionError:
            self.driver.quit()

    def tearDown(self):
        # Quit the browser
        self.driver.quit()



    def test_1_valid_text_home_btn(self):
        self.driver.maximize_window()
        self.driver.get('https://www.demoblaze.com/index.html')
        buttom = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, "/html/body/nav/div[1]/ul/li[1]/a")))
        buttom_text = buttom.text
        self.assertEqual(buttom_text, "Home")

    def test_2_valid_text_contact_btn(self):
        self.driver.maximize_window()
        self.driver.get('https://www.demoblaze.com/index.html')
        buttom = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="navbarExample"]/ul/li[2]/a')))
        buttom_text = buttom.text
        self.assertEqual(buttom_text, "Contact")

    def test_3_valid_text_about_us_btn(self):
        self.driver.maximize_window()
        self.driver.get('https://www.demoblaze.com/index.html')
        buttom = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="navbarExample"]/ul/li[3]/a')))
        buttom_text = buttom.text
        self.assertEqual(buttom_text, "About us")

    def test_4_valid_text_cart_btn(self):
        self.driver.maximize_window()
        self.driver.get('https://www.demoblaze.com/index.html')
        buttom = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="navbarExample"]/ul/li[4]/a')))
        buttom_text = buttom.text
        self.assertEqual(buttom_text, "Cart")

    def test_5_valid_text_log_in_btn(self):
        self.driver.maximize_window()
        self.driver.get('https://www.demoblaze.com/index.html')
        buttom = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="login2"]')))
        buttom_text = buttom.text
        expected_text = 'Log in'
        self.assertEqual(buttom_text, expected_text)

    def test_6_valid_text_sign_up_btn(self):
        self.driver.maximize_window()
        self.driver.get('https://www.demoblaze.com/index.html')
        buttom = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="signin2"]')))
        buttom_text = buttom.text
        self.assertEqual(buttom_text, "Sign up")

    def test_18_valid_text_sign_ip_btn(self):
        self.driver.maximize_window()
        self.driver.get('https://www.demoblaze.com/index.html')
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
        self.driver.maximize_window()
        self.driver.get('https://www.demoblaze.com/index.html')
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
        self.driver.maximize_window()
        self.driver.get('https://www.demoblaze.com/index.html')
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

    def test_40_add_prod_to_cart_valid(self):
        self.driver.maximize_window()
        self.driver.get('https://www.demoblaze.com/index.html')
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
        self.driver.maximize_window()
        self.driver.get('https://www.demoblaze.com/index.html')
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
        self.driver.maximize_window()
        self.driver.get('https://www.demoblaze.com/index.html')
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
        self.driver.maximize_window()
        self.driver.get('https://www.demoblaze.com/index.html')
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
        self.driver.maximize_window()
        self.driver.get('https://www.demoblaze.com/index.html')
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
