from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators1.home_locators import Buttons_home

class Homepage:

    def __init__(self, driver):
        self.driver = driver


    def txt_home_btn(self):
        title = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, Buttons_home.xpath_home_btn)))
        return title

    def txt_product_btn(self):
        title = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, Buttons_home.product_btn)))
        return title
    def txt_product_price(self):
        title = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, Buttons_home.product_price)))
        return title

    def previous_btn(self):
        title = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, Buttons_home.previous_btn)))
        return title

    def next_btn(self):
        title = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, Buttons_home.next_btn)))
        return title


    def txt_contact_btn(self):
        title = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, Buttons_home.xpath_contact_btn)))
        return title

    def txt_about_us_btn(self):
        title = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, Buttons_home.about_us_btn)))
        return title

    def txt_cart_btn(self):
        title = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, Buttons_home.cart_btn)))
        return title

    def txt_log_in_btn(self):
        title = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, Buttons_home.log_in_btn)))
        return title

    def txt_sign_up_btn(self):
        title = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, Buttons_home.sign_up_btn)))
        return title

    def txt_description(self):
        title = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, Buttons_home.product_descreption)))
        return title

    def click_home(self):
        WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.XPATH, Buttons_home.xpath_home_btn))).click()

    def click_contact(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, Buttons_home.xpath_contact_btn))).click()
    def click_about_us(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, Buttons_home.about_us_btn))).click()
    def click_cart(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, Buttons_home.cart_btn))).click()
    def click_login_btn(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, Buttons_home.log_in_btn))).click()
    def click_signup(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, Buttons_home.sign_up_btn))).click()
    def click_logo(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, Buttons_home.logo_btn))).click()
    def click_product_btn(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, Buttons_home.product_btn))).click()
    def click_previous_btn(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, Buttons_home.previous_btn))).click()

    def next_btn_click(self):
        title = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, Buttons_home.next_btn))).click()
