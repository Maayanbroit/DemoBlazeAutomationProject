from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators1.first_product_on_the_left_locators import Locators_product

class Product:

    def __init__(self, driver):
        self.driver = driver

    def inner_txt_product_btn(self):
        title = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, Locators_product.inner_product_btn)))
        return title

    def inner_product_image(self):
        image = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, Locators_product.inner_image)))
        return image


