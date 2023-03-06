import unittest
#import HtmlTestRunner
from pages.login_page import LoginPage
from utilities.driver import get_chrome_driver

class TestOH(unittest.TestCase):
    def setUp(self):
        try:
            self.driver = get_chrome_driver()
        except AssertionError:
            self.driver.quit()

    def tearDown(self):
        # Quit the browser
        self.driver.close()
        self.driver.quit()

    def test_valid_login(self):
        self.driver.maximize_window()
        self.driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
        # instantiate a class object of TestOH
        lp = LoginPage(self.driver)
        # call the Logging page method to fill user name field with argument username
        lp.set_username('Admin')
        # call the Logging page method to fill user name field with argument password
        lp.set_password('admin123')
        # call the Logging page method to click login button
        lp.click_login()
        assert self.driver.current_url == 'https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index'

    def test_invalid_login(self):
        self.driver.maximize_window()
        self.driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
        # instantiate a class object of TestOH
        lp = LoginPage(self.driver)
        # call the Logging page method to fill user name field with argument username
        lp.set_username('min')
        # call the Logging page method to fill user name field with argument password
        lp.set_password('admin123')
        # call the Logging page method to click login button
        lp.click_login()
        assert self.driver.current_url ==  'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'


if __name__ == '__main__':
    unittest.main()




    """replace test report"""
    #unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
    #   output='C:/Users/Elik/PycharmProjects/virtualEnvTutorial/tests/reports'))