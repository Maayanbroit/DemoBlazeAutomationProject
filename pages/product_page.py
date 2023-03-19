from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.product_locators import Locators_product
from time import sleep


class Product:

    def __init__(self, driver):
        self.driver = driver

    def txt_product_description(self):
        title = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, Locators_product.product_description)))
        return title

    def txt_add_to_cart(self):
        title = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, Locators_product.add_to_cart)))
        return title

    def click_add_to_cart(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, Locators_product.add_to_cart))).click()
        sleep(5)
    def inner_txt_product_btn(self):
        title = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, Locators_product.inner_product_btn)))
        return title

    def inner_product_image(self):
        image = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, Locators_product.inner_image)))
        return image


