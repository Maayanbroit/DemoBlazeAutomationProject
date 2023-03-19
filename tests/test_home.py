from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.setup import WebDriverSetup
from selenium.webdriver.common.by import By
from time import sleep

class TestOH(WebDriverSetup):


    def test_1_valid_text_home_btn(self):
        button = self.home_page.txt_home_btn()
        assert button.text == 'Home', f"Unexpected text: {button.text}"

    def test_2_valid_text_contact_btn(self):
        button = self.home_page.txt_contact_btn()
        assert button.text == 'Contact', f"Unexpected text: {button.text}"

    def test_3_valid_text_about_us_btn(self):
        button = self.home_page.txt_about_us_btn()
        assert button.text == 'About us', f"Unexpected text: {button.text}"

    def test_4_valid_text_cart_btn(self):
        button = self.home_page.txt_cart_btn()
        assert button.text == 'Cart', f"Unexpected text: {button.text}"

    def test_5_valid_text_log_in_btn(self):
        # Test if the text of the login button is correct
        button = self.home_page.txt_log_in_btn()
        assert button.text == 'Log in', f"Unexpected text: {button.text}"

    def test_6_valid_text_sign_up_btn(self):
        button = self.home_page.txt_sign_up_btn()
        assert button.text == 'Sign up', f"Unexpected text: {button.text}"

    def test_7_click_Home_btn(self):
        self.home_page.click_home()
        # Check if the current URL is correct
        assert self.driver.current_url == "https://www.demoblaze.com/index.html"

    def test_8_click_Contact_btn(self):
        self.home_page.click_contact()
        # Check if the contact popup is displayed
        assert self.home_page.contact_pop_up()

    def test_9_click_About_us_btn(self):
        self.home_page.click_about_us()
        # Check if the about us popup is displayed
        assert self.home_page.about_us_pop_up()

    def test_10_click_Cart_bnt(self):
        self.home_page.click_cart()
        # Check if the current URL is correct
        assert self.driver.current_url == "https://www.demoblaze.com/cart.html"

    def test_11_click_Log_in_btn(self):
        self.home_page.click_login_btn()
        # Check if the about us popup is displayed
        assert self.home_page.login_pop_up()

    def test_12_click_Sign_up_btn(self):
        self.home_page.click_signup()
        # Check if the about us popup is displayed
        assert self.home_page.sign_up_pop_up()

    def test_13_top_logo_redirect_home(self):
        self.home_page.click_logo()
        assert self.driver.current_url == 'https://www.demoblaze.com/index.html'

    def test_14_redirect_to_view_product_page(self):
        self.cart_page.click_samsung_6s()
        # check if the current URL is the product page
        assert self.driver.current_url == 'https://www.demoblaze.com/prod.html?idp_=1'

    def test_15_product_title(self):
        external_title = self.home_page.external_txt_product_btn()
        # Get the external text of the product button element
        external_title_text = external_title.text
        external_title.click()
        # Get the inner text of the product button element
        inner_title = self.product_page.inner_txt_product_btn()
        inner_title_text = inner_title.text
        #Check if the external and inner titles are equal
        assert external_title_text == inner_title_text
        print(external_title_text ,'\n', inner_title_text)

    def test_16_product_image(self):
        external_image = self.home_page.external_product_image()
        #get image source attribute
        external_image_src = external_image.get_attribute('src')
        external_image.click()
        inner_image = self.product_page.inner_product_image()
        inner_image_src = inner_image.get_attribute('src')
        # check if the external and inner image sources are equal
        self.assertEqual(external_image_src, inner_image_src)


    def test_17_scroll_down_home_page(self):
        self.scroll = self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(3)
        assert self.driver.execute_script("return window.scrollY") > 0, "Scrolling down the page not working"


    def test_18_valid_text_sign_ip_btn(self):
        description = self.home_page.txt_description().text
        self.home_page.click_product_btn()
        sleep(10)
        product_description = self.product_page.txt_product_description().text
        self.assertEqual(description, product_description)

    def test_19_valid_previous_btn(self):
        txt_product_btn = self.home_page.txt_product_btn().text
        self.home_page.click_previous_btn()
        sleep(5)
        left_corn_product_after = self.home_page.txt_product_btn().text
        self.assertNotEqual(txt_product_btn, left_corn_product_after)

    def test_20_valid_next_btn(self):
        left_corn_product = self.home_page.txt_product_btn().text
        self.home_page.next_btn_click()
        sleep(5)
        left_corn_product_after = self.home_page.txt_product_btn().text
        self.assertNotEqual(left_corn_product, left_corn_product_after)


    def test_21_next_button_displayed_previous_not(self):
        self.scroll = self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # check if next button is displayed and previous button not
        is_next_btn_displayed = self.home_page.next_product_btn_id
        is_previous_btn_displayed = self.home_page.previous_product_btn_id
        assert is_previous_btn_displayed == False and is_next_btn_displayed == True

    def test_22_previous_button_displayed_next_not(self):
        self.scroll = self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Click next button to go to the next image
        is_next_btn_display = self.home_page.next_product_btn_click_id()
        sleep(5)
        is_previous_btn_displayed = self.home_page.previous_product_btn_id()
        next_btn = self.home_page.next_product_btn_id()
        # Check if previous button is displayed and next button is not
        assert is_previous_btn_displayed == True and next_btn == False


    def test_27_image_bar_r_btn(self):
        # click the right button in the image bar
        self.home_page.click_image_bar_r_btn()
        # Check if the first image is not the same as the second image
        image_1 = self.home_page.image_1()
        image_2 = self.home_page.image_2()
        sleep(3)
        self.assertNotEqual(image_1, image_2)

    def test_28_image_bar_l_btn(self):
        # click the left button in the image bar
        self.home_page.click_image_bar_l_btn()
        # Check if the first image is not the same as the second image
        image_1 = self.home_page.image_1()
        image_3 = self.home_page.image_3()
        sleep(3)
        self.assertNotEqual(image_1, image_3)

    def test_29_about_as_text(self):
        # Scroll down the page to find the text
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Check if the 'about us' text is displayed
        assert self.home_page.about_us_text()

    def test_30_get_in_touch_text(self):
        # Scroll down the page to find the text
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Check if the 'get in touch' text is displayed
        assert self.home_page.get_in_touch_text()