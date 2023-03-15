from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.setup import WebDriverSetup
from selenium.webdriver.common.by import By
from time import sleep


class TestOH(WebDriverSetup):


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
        # Click the samsung_6s button
        self.cart_page.click_samsung_6s()
        # Click the add cart button
        self.cart_page.click_add_cart()
        # Alert is displayed
        alert = WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        alert.accept()
        # Click the cart button
        self.cart_page.click_cart_btn()
        # Click the delete button
        self.cart_page.click_delete_btn()
        assert self.driver.find_element(By.XPATH, '/html/body/div[6]/div/div[2]').is_displayed()

    def test_46_place_order(self):
        # Click the cart button
        self.cart_page.click_cart_btn()
        # Click the place order button
        self.cart_page.click_place_order_btn()
        assert WebDriverWait(self.driver, 5).until(EC.invisibility_of_element_located((By.XPATH, "/html/body/div[3]/div/div")))


    def test_47_valid_order_without_login(self):
        self.cart_page.click_product()
        self.cart_page.click_add_cart()
        alert = WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        alert.accept()
        sleep(2)
        self.cart_page.click_cart_btn()
        sleep(2)
        self.cart_page.click_place_order_btn()
        self.cart_page.fill_name('Shiran')
        self.cart_page.fill_country('Israel')
        self.cart_page.fill_city('Kfar Yona')
        self.cart_page.fill_card('552211')
        self.cart_page.fill_month('5')
        self.cart_page.fill_year('2030')
        self.cart_page.click_purchase()
        sleep(3)
        assert self.driver.find_element(By.XPATH, '/html/body/div[9]').is_displayed()

    def test_48_purchase_button_disable(self):
        self.cart_page.click_product()
        self.cart_page.click_add_cart()
        alert = WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        alert.accept()
        self.cart_page.click_cart_btn()
        self.cart_page.click_place_order_btn()
        self.cart_page.fill_name('Shiran')
        self.cart_page.fill_country('Israel')
        self.cart_page.fill_city('Kfar Yona')
        self.cart_page.fill_card('552211')
        self.cart_page.fill_month('5')
        self.cart_page.fill_year('2030')
        self.cart_page.click_purchase()
        sleep(2)
        is_purchase_btn_enabled = self.cart_page.check_is_purchase_btn_enabled()
        print(is_purchase_btn_enabled)
        assert is_purchase_btn_enabled == False

    def test_49_empty_order_without_login(self):
        self.cart_page.click_cart_btn()
        self.cart_page.click_place_order_btn()
        self.cart_page.fill_name('Shiran')
        self.cart_page.fill_country('Israel')
        self.cart_page.fill_city('Kfar Yona')
        self.cart_page.fill_card('552211')
        self.cart_page.fill_month('5')
        self.cart_page.fill_year('2030')
        sleep(2)
        self.cart_page.click_purchase()
        sleep(2)
        assert WebDriverWait(self.driver, 5).until(EC.invisibility_of_element_located((By.XPATH, '/html/body/div[9]')))

    def test_50_valid_order_with_login(self):
        self.login_page.click_log_in_btn()
        self.login_page.set_username('Bdika')
        self.login_page.set_password('123')
        self.login_page.click_login()
        sleep(3)
        self.cart_page.click_product()
        sleep(3)
        self.cart_page.click_add_cart()
        alert = WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        alert.accept()
        self.cart_page.click_cart_btn()
        self.cart_page.click_place_order_btn()
        self.cart_page.fill_name('Shiran')
        self.cart_page.fill_country('Israel')
        self.cart_page.fill_city('Kfar Yona')
        self.cart_page.fill_card('552211')
        self.cart_page.fill_month('5')
        self.cart_page.fill_year('2030')
        self.cart_page.click_purchase()
        sleep(2)

        assert self.driver.find_element(By.XPATH, '/html/body/div[9]').is_displayed()

    def test_51_empty_order_with_login(self):
        self.login_page.click_log_in_btn()
        self.login_page.set_username('Bdika')
        self.login_page.set_password('123')
        self.login_page.click_login()
        sleep(3)
        self.cart_page.click_cart_btn()
        self.cart_page.click_place_order_btn()
        self.cart_page.fill_name('Shiran')
        self.cart_page.fill_country('Israel')
        self.cart_page.fill_city('Kfar Yona')
        self.cart_page.fill_card('552211')
        self.cart_page.fill_month('5')
        self.cart_page.fill_year('2030')
        self.cart_page.click_purchase()
        sleep(5)
        assert WebDriverWait(self.driver, 5).until(EC.invisibility_of_element_located((By.XPATH, '/html/body/div[9]')))
