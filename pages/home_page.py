from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.home_locators import Buttons_home
from time import sleep


class Homepage:

    def __init__(self, driver):
        self.driver = driver


    def txt_home_btn(self):
        title = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, Buttons_home.xpath_home_btn)))
        return title

    def txt_product_btn(self):
        title = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, Buttons_home.product_btn)))
        return title


    def external_txt_product_btn(self):
        title = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, Buttons_home.external_product_btn)))
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


    def external_product_image(self):
        image = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, Buttons_home.external_image)))
        return image

    def next_product_btn_id(self):
       # title = WebDriverWait(self.driver, 5).until(
       #      EC.visibility_of_element_located((By.ID, Buttons_home.next_btn))).is_displayed()
      title  = self.driver.find_element(By.ID, Buttons_home.next_btn_id).is_displayed()
      return title

    def next_product_btn_click_id(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.ID, Buttons_home.next_btn_id))).click()

    def previous_product_btn_id(self):
       title = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.ID, Buttons_home.previous_btn_id))).is_displayed()
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
        WebDriverWait(self.driver, 5)
    def click_contact(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, Buttons_home.xpath_contact_btn))).click()
        sleep(2)
    def click_about_us(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, Buttons_home.about_us_btn))).click()
        sleep(2)
    def click_cart(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, Buttons_home.cart_btn))).click()
        sleep(5)
    def click_login_btn(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, Buttons_home.log_in_btn))).click()
        sleep(2)
    def click_signup(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, Buttons_home.sign_up_btn))).click()
        sleep(2)
    def click_logo(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, Buttons_home.logo_btn))).click()

    def click_image_bar_r_btn(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, Buttons_home.image_bar_r_btn))).click()

    def click_image_bar_l_btn(self):
         WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, Buttons_home.image_bar_l_btn))).click()

    def image_1(self):
         image_1 = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, Buttons_home.image_1)))
         return image_1

    def image_2 (self):
        image_2 = WebDriverWait(self.driver, 10).until( EC.visibility_of_element_located((By.XPATH, Buttons_home.image_2)))
        return image_2

    def image_3 (self):
        image_3 = WebDriverWait(self.driver, 10).until( EC.visibility_of_element_located((By.XPATH, Buttons_home.image_3)))
        return image_3
    def click_product_btn(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, Buttons_home.product_btn))).click()
    def click_previous_btn(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, Buttons_home.previous_btn))).click()

    def next_btn_click(self):
        title = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, Buttons_home.next_btn))).click()

    def about_us_text(self):
        text = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, Buttons_home.about_us_text))).is_displayed()
        return text

    def get_in_touch_text(self):
        text = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, Buttons_home.get_in_touch_text))).is_displayed()
        return text

    #assert tests 7-12:
    def contact_pop_up(self):
        x = self.driver.find_element(By.XPATH, Buttons_home.contact_pop_up).is_displayed()
        return x
    def about_us_pop_up(self):
        x = self.driver.find_element(By.XPATH, Buttons_home.about_us_pop_up).is_displayed()
        return x
    def login_pop_up(self):
        x = self.driver.find_element(By.XPATH, Buttons_home.login_pop_up).is_displayed()
        return x
    def sign_up_pop_up(self):
        x = self.driver.find_element(By.XPATH, Buttons_home.sign_up_pop_up).is_displayed()
        return x