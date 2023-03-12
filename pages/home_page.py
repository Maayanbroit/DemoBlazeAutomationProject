from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from locators.login_page_locators import LoginLocators

class LoginPage:

    username_text = 'loginusername'
    password_text = 'loginpassword'
    login_xpath = '//*[@id="logInModal"]/div/div/div[3]/button[2]'
    close_xpath = '//*[@id="logInModal"]/div/div/div[3]/button[1]'

    def __init__(self, driver):
        self.driver = driver
    def set_username(self, username):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID,self.username_text))).send_keys(username)
    def set_password(self, password):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID,self.password_text))).send_keys(password)
    def click_login(self):
        WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.XPATH,self.login_xpath))).click()
    def click_close_login(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH,self.close_xpath))).click()


class Buttons:

    home_btn = "/html/body/nav/div[1]/ul/li[1]/a"
    contact_btn = "/html/body/nav/div[1]/ul/li[2]/a"
    about_us_btn = "/html/body/nav/div[1]/ul/li[3]/a"
    cart_btn = '//*[@id="cartur"]'
    log_in_btn = "/html/body/nav/div[1]/ul/li[5]/a"
    sign_up_btn = "/html/body/nav/div[1]/ul/li[8]/a"
    logo_btn = 'nava'
    product_btn = '//*[@id="tbodyid"]/div[1]/div/div/h4/a'
    add_cart_btn = '//*[@id="tbodyid"]/div[2]/div/a'
    place_order_btn = '//*[@id="page-wrapper"]/div/div[2]/button'
    purchase_btn = '//*[@id="orderModal"]/div/div/div[3]/button[2]'


    def __init__(self,driver):
        self.driver = driver
    def click_home(self):
        WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.XPATH,self.home_btn))).click()
    def click_contact(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH,self.contact_btn))).click()
    def click_about_us(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH,self.about_us_btn))).click()
    def click_cart(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH,self.cart_btn))).click()
    def click_login_btn(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH,self.log_in_btn))).click()
    def click_signup(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH,self.sign_up_btn))).click()
    def click_logo(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID,self.logo_btn))).click()
    def click_product(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, self.product_btn))).click()
    def click_add_cart(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, self.add_cart_btn))).click()
    def click_place_order(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, self.place_order_btn))).click()
    def click_purchase(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, self.purchase_btn))).click()
    def check_is_purchase_btn_enabled(self):
        return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, self.purchase_btn))).is_enabled()


class ValidOrder:
    name_field = 'name'
    country_field = 'country'
    city_field = 'city'
    credit_card_field = 'card'
    month_field = 'month'
    year_field = 'year'
    def __init__(self, driver):
        self.driver = driver
    def fill_name(self, name):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, self.name_field))).send_keys(name)
    def fill_country(self, country):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, self.country_field))).send_keys(country)
    def fill_city(self, city):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, self.city_field))).send_keys(city)
    def fill_card(self, card):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, self.credit_card_field))).send_keys(card)
    def fill_month(self, month):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, self.month_field))).send_keys(month)
    def fill_year(self, year):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, self.year_field))).send_keys(year)
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
