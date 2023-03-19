from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.setup import WebDriverSetup
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains



class TestOH(WebDriverSetup):

    def test_40_add_prod_to_cart_valid(self):
        txt_product_btn = self.home_page.txt_product_btn().text
        self.home_page.click_product_btn()
        self.product_page.click_add_to_cart()
        alert = self.driver.switch_to.alert
        alert.accept()
        self.home_page.click_cart()
        title_in_cart = self.cart_page.txt_product().text
        self.assertEqual(txt_product_btn, title_in_cart)

    def test_41_add_3times_prod_to_cart_valid(self):
        txt_product_btn_1 = self.home_page.txt_product_btn().text
        self.home_page.click_product_btn()
        self.product_page.click_add_to_cart()
        alert = self.driver.switch_to.alert
        alert.accept()
        self.product_page.click_add_to_cart()
        alert = self.driver.switch_to.alert
        alert.accept()
        self.product_page.click_add_to_cart()
        alert = self.driver.switch_to.alert
        alert.accept()
        self.home_page.click_cart()
        title_in_cart_1 = self.cart_page.txt_product().text
        self.assertEqual(txt_product_btn_1, title_in_cart_1)

        title_in_cart_2 = self.cart_page.txt_product_2().text
        self.assertEqual(txt_product_btn_1, title_in_cart_2)

        title_in_cart_3 = self.cart_page.txt_product_3().text
        self.assertEqual(txt_product_btn_1, title_in_cart_3)

    def test_42_prod_add_popup_valid(self):
        self.home_page.click_product_btn()
        self.product_page.click_add_to_cart()
        alert = WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        self.assertEqual(alert.text, "Product added")
        alert = self.driver.switch_to.alert
        alert.accept()

    def test_43_prod_price_valid(self):
        left_corn_product_price = self.home_page.txt_product_price().text
        self.home_page.click_product_btn()
        self.product_page.click_add_to_cart()
        alert = self.driver.switch_to.alert
        alert.accept()
        self.home_page.click_cart()
        price_in_cart = self.cart_page.txt_price_in_cart().text
        self.assertEqual(price_in_cart, left_corn_product_price)

    def test_44_del_prod_from_cart_valid(self):
        left_corn_product = self.home_page.txt_product_btn().text
        self.home_page.click_product_btn()
        self.product_page.click_add_to_cart()
        alert = self.driver.switch_to.alert
        alert.accept()
        self.home_page.click_cart()
        title_in_cart = self.cart_page.txt_product().text
        self.assertEqual(left_corn_product, title_in_cart)
        self.cart_page.click_delete_btn()
        sleep(5)
        assert self.cart_page.txt_product_invisibility()

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
        sleep(2)
        assert self.cart_page.total()

    def test_46_place_order(self):
        # Click the cart button
        self.cart_page.click_cart_btn()
        # Click the place order button
        self.cart_page.click_place_order_btn()
        assert self.cart_page.place_order_popup() == False



    def test_47_valid_order_without_login(self):
        self.cart_page.click_samsung_6s()
        self.cart_page.click_add_cart()
        alert = WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        alert.accept()
        self.cart_page.fill_place_order_fields()
        assert self.cart_page.purchase_confirmation_popup()

    def test_48_purchase_button_disable(self):
        self.cart_page.click_samsung_6s()
        self.cart_page.click_add_cart()
        alert = WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        alert.accept()
        self.cart_page.fill_place_order_fields()
        is_purchase_btn_enabled = self.cart_page.check_is_purchase_btn_enabled()
        assert is_purchase_btn_enabled == False

    def test_49_empty_order_without_login(self):
        self.cart_page.fill_place_order_fields()
        assert self.cart_page.purchase_confirmation_popup() == False


    def test_50_valid_order_with_login(self):
        self.login_page.log_in_process()
        sleep(3)
        self.cart_page.click_samsung_6s()
        self.cart_page.click_add_cart()
        alert = WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        alert.accept()
        self.cart_page.fill_place_order_fields()
        assert self.cart_page.purchase_confirmation_popup()


    def test_51_empty_order_with_login(self):
        self.login_page.log_in_process()
        sleep(3)
        self.cart_page.fill_place_order_fields()
        assert self.cart_page.purchase_confirmation_popup() == False
