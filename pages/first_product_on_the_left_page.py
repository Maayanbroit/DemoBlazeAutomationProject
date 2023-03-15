from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators1.cart_locators import Cart_Locators



def click_samsung_6s(self):
    WebDriverWait(self.driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, Cart_Locators.samsung_galaxy_s6))).click()