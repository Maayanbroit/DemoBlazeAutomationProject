
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.cart_locators import Cart_Locators
from time import sleep

class Cartpage:

    def __init__(self, driver):
        self.driver = driver

    def click_cart_btn(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, Cart_Locators.cart_btn))).click()

    def click_place_order_btn(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, Cart_Locators.place_order_btn))).click()
        sleep(3)

    def click_product(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, Cart_Locators.product_btn))).click()

    def txt_product(self):
        title = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, Cart_Locators.product_btn)))
        return title
    def txt_product_invisibility(self):
        title = WebDriverWait(self.driver, 5).until(EC.invisibility_of_element_located((By.XPATH, Cart_Locators.product_btn)))
        return title
    def txt_product_2(self):
        title = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, Cart_Locators.product_2_btn)))
        return title
    def total(self):
        title = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, Cart_Locators.total))).is_displayed()
        return title

    def txt_product_3(self):
        title = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, Cart_Locators.product_3_btn)))
        return title
    def txt_price_in_cart(self):
        title = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, Cart_Locators.price_in_cart)))
        return title

    def click_add_cart(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH,  Cart_Locators.add_cart_btn))).click()

    def click_purchase(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, Cart_Locators.purchase_btn))).click()

    def check_is_purchase_btn_enabled(self):
        return WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, Cart_Locators.purchase_btn))).is_enabled()

    def click_delete_btn(self):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH, Cart_Locators.delete_btn))).click()

    def click_samsung_6s(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, Cart_Locators.samsung_galaxy_s6))).click()


    def fill_name(self, name):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, Cart_Locators.name_field))).send_keys(name)

    def fill_country(self, country):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, Cart_Locators.country_field))).send_keys(country)

    def fill_city(self, city):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, Cart_Locators.city_field))).send_keys(city)

    def fill_card(self, card):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, Cart_Locators.credit_card_field))).send_keys(card)

    def fill_month(self, month):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, Cart_Locators.month_field))).send_keys(month)

    def fill_year(self, year):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, Cart_Locators.year_field))).send_keys(year)

    def fill_place_order_fields(self):
        self.click_cart_btn()
        self.click_place_order_btn()
        self.fill_name('Shiran')
        self.fill_country('Israel')
        self.fill_city('Kfar Yona')
        self.fill_card('552211')
        self.fill_month('5')
        self.fill_year('2030')
        self.click_purchase()


    def place_order_popup(self):
        popup = self.driver.find_element(By.XPATH, Cart_Locators.place_order_popup).is_displayed()
        return popup

    def purchase_confirmation_popup(self):
       popup = self.driver.find_element(By.XPATH, Cart_Locators.purchase_success_popup).is_displayed()
       return popup

