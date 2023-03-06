from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.login_page_locators import LoginLocators
from selenium.webdriver.chrome.service import Service
from time import sleep

class Buttons:
    image_bar_r_btn = "/html/body/nav/div[2]/div/a[2]"
    image_bar_l_btn = "/html/body/nav/div[2]/div/a[1]"
    # image_1 = "/html/body/nav/div[2]/div/div/div[1]/img"
    # image_2 = "/html/body/nav/div[2]/div/div/div[2]/img"
    # image_3 = "/html/body/nav/div[2]/div/div/div[3]/img"


    def __init__(self, driver):
        self.driver = driver
    def click_image_r(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, self.image_bar_r_btn))).click()

    def click_image_l(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, self.image_bar_l_btn))).click()




class Footer:
    # class attributes
    about_us_text = '/html/body/div[6]/div/div[1]'
    get_in_touch_text = '/html/body/div[6]/div/div[2]'

    def __init__(self, driver):
        self.driver = driver

    def aboutus_text(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, self.about_us_text)))


class Log_in:
    Log_in_btn_above = "/html/body/nav/div[1]/ul/li[5]/a"
    user_name = "/html/body/div[3]/div/div/div[2]/form/div[1]/input"
    password = "/html/body/div[3]/div/div/div[2]/form/div[2]/input"
    login_xpath = '/html/body/div[3]/div/div/div[3]/button[2]'
    Log_out_btn = "/html/body/nav/div[1]/ul/li[6]/a"

    def __init__(self, driver):
        self.driver = driver

    def click_log_in_btn(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, self.Log_in_btn_above))).click()
    def set_username(self, username):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH,self.user_name))).send_keys(username)
    def set_password(self, password):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH,self.password))).send_keys(password)
    def click_login(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH,self.login_xpath))).click()
    def click_logout(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH,self.Log_out_btn))).click()



class Contact:
      contact_btn = "/html/body/nav/div[1]/ul/li[2]/a"
      email = "/html/body/div[1]/div/div/div[2]/form/div[1]/input"
      name = "/html/body/div[1]/div/div/div[2]/form/div[2]/input"
      message = "/html/body/div[1]/div/div/div[2]/form/div[3]/textarea"
      send_message_btn = "/html/body/div[1]/div/div/div[3]/button[2]"
      close_btn = "/html/body/div[1]/div/div/div[3]/button[1]"


      def __init__(self, driver):
          self.driver = driver

      def click_contact_btn(self):
          WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, self.contact_btn))).click()

      def set_email(self, email):
          WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, self.email))).send_keys(email)

      def set_name(self, name):
          WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, self.name))).send_keys(name)

      def set_message(self, message):
          WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, self.message))).send_keys(message)
          return message

      def click_send_message(self):
          WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, self.send_message_btn))).click()


      def click_close_btn(self):
          WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, self.close_btn))).click()



class Cart:
      samsung_galaxy_s6 = "/html/body/div[5]/div/div[2]/div/div[1]/div/div/h4/a"
      add_to_cart = "/html/body/div[5]/div/div[2]/div[2]/div/a"
      cart_btn = "/html/body/nav/div/div/ul/li[4]/a"
      delete_btn = "/html/body/div[6]/div/div[1]/div/table/tbody/tr/td[4]/a"
      Total = "/html/body/div[6]/div/div[2]"
      place_order_btn = "/html/body/div[6]/div/div[2]/button"
      Place_order = "/html/body/div[3]/div/div"

      def __init__(self, driver):
          self.driver = driver

      def click_samsung_6s(self):
          WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, self.samsung_galaxy_s6))).click()

      def click_add_btn(self):
          WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, self.add_to_cart))).click()

      def click_cart_btn(self):
          WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, self.cart_btn))).click()

      def click_delete_btn(self):
          WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, self.delete_btn))).click()

      def click_place_order_btn(self):
          WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, self.place_order_btn))).click()