
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.meshi_page import Buttons
from pages.meshi_page import Sigh_up
from utilities.driver import get_chrome_driver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import string

class Test_Store(unittest.TestCase):

    def setUp(self):
        try:
            self.driver = get_chrome_driver()
        except AssertionError:
            self.driver.quit()


    def tearDown(self):
        self.driver.quit()

    def test_7_click_Home_btn(self):
        self.driver.maximize_window()
        self.driver.get('https://www.demoblaze.com/index.html')
        c_page = Buttons(self.driver)
        c_page.click_Home()
        sleep(2)
        assert self.driver.current_url == "https://www.demoblaze.com/index.html"

    def test_8_click_Contact_btn(self):
        self.driver.maximize_window()
        self.driver.get('https://www.demoblaze.com/index.html')
        c_page = Buttons(self.driver)
        c_page.click_Contact()
        sleep(2)
        assert self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div").is_displayed()


    def test_9_click_About_us_btn(self):
        self.driver.maximize_window()
        self.driver.get('https://www.demoblaze.com/index.html')
        c_page = Buttons(self.driver)
        c_page.click_About_us()
        sleep(2)
        assert self.driver.find_element(By.XPATH, "/html/body/div[4]/div/div").is_displayed()

    def test_10_click_Cart_bnt(self):
        self.driver.maximize_window()
        self.driver.get('https://www.demoblaze.com/index.html')
        c_page = Buttons(self.driver)
        c_page.click_Cart()
        sleep(2)
        assert self.driver.current_url == "https://www.demoblaze.com/cart.html"

    def test_11_click_Log_in_btn(self):
        self.driver.maximize_window()
        self.driver.get('https://www.demoblaze.com/index.html')
        c_page = Buttons(self.driver)
        c_page.click_Login()
        sleep(2)
        assert self.driver.find_element(By.XPATH , "/html/body/div[3]/div/div").is_displayed()


    def test_12_click_Sigh_up_btn(self):
        self.driver.maximize_window()
        self.driver.get('https://www.demoblaze.com/index.html')
        c_page = Buttons(self.driver)
        c_page.click_Sighup()
        sleep(2)
        assert self.driver.find_element(By.XPATH , "/html/body/div[2]/div/div").is_displayed()


    def test_37_send_empty_message(self):
        self.driver.maximize_window()
        self.driver.get('https://www.demoblaze.com/index.html')
        c_page = Buttons(self.driver)
        c_page.click_Contact()
        c_page.click_send_message()
        sleep(2)
        alert = WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        self.assertEqual(alert.text, "Details not filled in.")

    def test_38_About_us_video(self):
        self.driver.maximize_window()
        self.driver.get('https://www.demoblaze.com/index.html')
        c_page = Buttons(self.driver)
        c_page.click_About_us()
        sleep(2)
        c_page.click_play_video()
        sleep(2)
        assert self.driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div[2]/form/div/div/video").is_enabled()

    def test_39_About_us_close(self):
        self.driver.maximize_window()
        self.driver.get('https://www.demoblaze.com/index.html')
        c_page = Buttons(self.driver)
        c_page.click_About_us()
        WebDriverWait(self.driver, 5)
        c_page.click_about_us_close()
        assert WebDriverWait(self.driver, 5).until(EC.invisibility_of_element_located((By.XPATH, "/html/body/div[4]/div/div")))

    def test_53_Sign_up_with_valid_details(self):
        self.driver.maximize_window()
        self.driver.get('https://www.demoblaze.com/index.html')
        c_page = Buttons(self.driver)
        c_page.click_Sighup()
        WebDriverWait(self.driver, 5)
        c_page1 = Sigh_up(self.driver)

        str1 = ""
        for i in range(6):
            x = random.choice(string.ascii_letters)
            str1 = str1 + x

        c_page1.set_username(str1)
        WebDriverWait(self.driver, 5)
        c_page1.set_password("123")
        WebDriverWait(self.driver, 5)
        c_page1.click_sigh_us_in_pop()
        sleep(2)
        alert = WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        self.assertEqual(alert.text, "Sign up successful.")

    def test_54_Sign_up_with_exists_user(self):
        self.driver.maximize_window()
        self.driver.get('https://www.demoblaze.com/index.html')
        c_page = Buttons(self.driver)
        c_page.click_Sighup()
        WebDriverWait(self.driver, 5)
        c2_page = Sigh_up(self.driver)
        c2_page.set_username("bdika1")
        WebDriverWait(self.driver, 5)
        c2_page.set_password("123")
        WebDriverWait(self.driver, 5)
        c2_page.click_sigh_us_in_pop()
        sleep(2)
        alert = WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        self.assertEqual(alert.text, "This user already exist.")

    def test_55_Sigh_up_close(self):
        self.driver.maximize_window()
        self.driver.get('https://www.demoblaze.com/index.html')
        c_page = Buttons(self.driver)
        c_page.click_Sighup()
        WebDriverWait(self.driver, 5)
        c_page.click_sigh_up_close()
        sleep(2)
        assert WebDriverWait(self.driver, 5).until(
            EC.invisibility_of_element_located((By.XPATH, "/html/body/div[2]/div/div")))

    def test_56_Sigh_up_username_max_10_char(self):
        self.driver.maximize_window()
        self.driver.get('https://www.demoblaze.com/index.html')
        c_page = Buttons(self.driver)
        c_page.click_Sighup()
        WebDriverWait(self.driver, 5)
        c_page1 = Sigh_up(self.driver)

        str1 = ""
        for i in range(11):
            x = random.choice(string.ascii_letters)
            str1 = str1 + x

        username = c_page1.set_username(str1)
        WebDriverWait(self.driver, 5)
        c_page1.set_password("123")
        WebDriverWait(self.driver, 5)
        c_page1.click_sigh_us_in_pop()
        sleep(2)
        alert = WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        if len(username) <= 10:
            self.assertEqual(alert.text, "Sign up successful.")
        else:
            self.assertEqual(alert.text, "You need a maximum of 10 characters in the user name.")

    def test_59_send_empty_Sigh_up(self):
        self.driver.maximize_window()
        self.driver.get('https://www.demoblaze.com/index.html')
        c_page = Buttons(self.driver)
        c_page.click_Sighup()
        WebDriverWait(self.driver, 5)
        c_page1 = Sigh_up(self.driver)
        c_page1.click_sigh_us_in_pop()
        sleep(2)
        alert = WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        self.assertEqual(alert.text, "Please fill out Username and Password.")



if __name__ == '__main__':
    unittest.main()

