
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class Buttons:

    home_btn = "/html/body/nav/div[1]/ul/li[1]/a"
    contact_btn = "/html/body/nav/div[1]/ul/li[2]/a"
    about_us_btn = "/html/body/nav/div[1]/ul/li[3]/a"
    cart_btn = "/html/body/nav/div[1]/ul/li[4]/a"
    log_in_btn = "/html/body/nav/div[1]/ul/li[5]/a"
    sign_in_btn = "/html/body/nav/div[1]/ul/li[8]/a"

    send_message_btn = "/html/body/div[1]/div/div/div[3]/button[2]"
    play_video_btn = "/html/body/div[4]/div/div/div[2]/form/div/div/button"
    about_us_close_btn = "/html/body/div[4]/div/div/div[3]/button"
    sigh_up_close_btn = "/html/body/div[2]/div/div/div[3]/button[1]"

    def __init__(self,driver):
        self.driver = driver


    def click_Home(self):
        WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.XPATH,self.home_btn))).click()

    def click_Contact(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, self.contact_btn))).click()

    def click_About_us(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, self.about_us_btn))).click()

    def click_Cart(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, self.cart_btn))).click()

    def click_Login(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, self.log_in_btn))).click()

    def click_Sighup(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, self.sign_in_btn))).click()

    def click_send_message(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, self.send_message_btn))).click()

    def click_play_video(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, self.play_video_btn))).click()

    def click_about_us_close(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, self.about_us_close_btn))).click()

    def click_sigh_up_close(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, self.sigh_up_close_btn))).click()


class Sigh_up:

    user_name_text = "sign-username"
    password_text = "sign-password"
    sigh_up_xpath = "/html/body/div[2]/div/div/div[3]/button[2]"

    def __init__(self,driver):
        self.driver = driver

    def set_username(self, username):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, self.user_name_text))).send_keys(
            username)
        return username

    def set_password(self, password):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, self.password_text))).send_keys(
            password)

    def click_sigh_us_in_pop(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, self.sigh_up_xpath))).click()






