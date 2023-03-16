import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.cart_page import Cartpage
from pages.home_page import Homepage
from pages.contact_page import Contactpage
from pages.about_us_page import About_As_page
from pages.login_page import LoginPage
from pages.sign_up_page import Sign_Up_Page
from selenium.webdriver.chrome.options import Options
from pages.product_page import Product

class WebDriverSetup(unittest.TestCase):
    def setUp(self) -> None:
        try:
            chromedriver_path = "C:/Webdriver/chromedriver.exe"
            service = Service(executable_path=chromedriver_path)
            # options = Options()
            #options.headless = True
            options = webdriver.ChromeOptions()
            options.add_argument("--disable-extensions")
            self.driver = webdriver.Chrome(service=service,options=options)
            self.driver.maximize_window()
            self.driver.set_page_load_timeout(30)
            self.driver.get("https://www.demoblaze.com/index.html")
            self.login_page = LoginPage(self.driver)
            self.home_page = Homepage(self.driver)
            self.contact_page = Contactpage(self.driver)
            self.about_us_page = About_As_page(self.driver)
            self.cart_page = Cartpage(self.driver)
            self.sign_up_page = Sign_Up_Page(self.driver)
            self.product_page = Product(self.driver)
            time.sleep(1)

        except AssertionError:
            self.driver.quit()

    def tearDown(self) -> None:
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
