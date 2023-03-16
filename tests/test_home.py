from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.setup import WebDriverSetup
from selenium.webdriver.common.by import By
from time import sleep

class TestOH(WebDriverSetup):


    def test_1_valid_text_home_btn(self):
        button = self.home_new_page.txt_home_btn()
        assert button.text == 'Home', f"Unexpected text: {button.text}"

    def test_2_valid_text_contact_btn(self):
        button = self.home_new_page.txt_contact_btn()
        assert button.text == 'Contact us', f"Unexpected text: {button.text}"

    def test_3_valid_text_about_us_btn(self):
        button = self.home_new_page.txt_about_us_btn()
        assert button.text == 'About us', f"Unexpected text: {button.text}"

    def test_4_valid_text_cart_btn(self):
        button = self.home_new_page.txt_cart_btn()
        assert button.text == 'Cart', f"Unexpected text: {button.text}"

    def test_5_valid_text_log_in_btn(self):
        # Test if the text of the login button is correct
        button = self.home_new_page.txt_log_in_btn()
        assert button.text == 'Log in', f"Unexpected text: {button.text}"

    def test_6_valid_text_sign_up_btn(self):
        button = self.home_new_page.txt_sign_up_btn()
        assert button.text == 'Sign up', f"Unexpected text: {button.text}"

    def test_7_click_Home_btn(self):
        self.home_new_page.click_home()
        # Check if the current URL is correct
        assert self.driver.current_url == "https://www.demoblaze.com/index.html"

    def test_8_click_Contact_btn(self):
        self.home_new_page.click_contact()
        # Check if the contact popup is displayed
        assert self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div").is_displayed()

    def test_9_click_About_us_btn(self):
        self.home_new_page.click_about_us()
        # Check if the about us popup is displayed
        assert self.driver.find_element(By.XPATH, "/html/body/div[4]/div/div").is_displayed()

    def test_10_click_Cart_bnt(self):
        self.home_new_page.click_cart()
        # Check if the current URL is correct
        assert self.driver.current_url == "https://www.demoblaze.com/cart.html"

    def test_11_click_Log_in_btn(self):
        self.home_new_page.click_login_btn()
        # Check if the about us popup is displayed
        assert self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div").is_displayed()

    def test_12_click_Sign_up_btn(self):
        self.home_new_page.click_signup()
        # Check if the about us popup is displayed
        assert self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div").is_displayed()

    def test_13_top_logo_redirect_home(self):
        self.home_new_page.click_logo()
        sleep(5)
        assert self.driver.current_url == 'https://www.demoblaze.com/index.html'

    def test_14_redirect_to_view_product_page(self):
        self.home_new_page.click_product()
        sleep(3)
        # check if the current URL is the product page
        assert self.driver.current_url == 'https://www.demoblaze.com/prod.html?idp_=1'

    def test_15_product_title(self):
        external_title = self.home_new_page.txt_product_btn()
        # Get the external text of the product button element
        external_title_text = external_title.text
        print(external_title_text)
        external_title.click()
        sleep(3)
        # Get the inner text of the product button element
        inner_title = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="tbodyid"]/h2')))
        internal_title_text = inner_title.text
        print(internal_title_text)
        sleep(2)
        #Check if the external and inner titles are equal
        assert external_title_text == internal_title_text

    def test_16_product_image(self):
        external_image = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="tbodyid"]/div[1]/div/a/img')))
        #get image source attribute
        external_image_src = external_image.get_attribute('src')
        external_image.click()
        inner_image = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="imgp"]/div/img')))
        inner_image_src = inner_image.get_attribute('src')
        sleep(5)
        print(inner_image_src)
        # check if the external and inner image sources are equal
        self.assertEqual(external_image_src, inner_image_src)

    def test_17_scroll_down_home_page(self):
        sleep(5)
        scroll = self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(5)
        assert self.driver.execute_script("return window.scrollY") > 0, "Scrolling down the page not working"

    def test_18_valid_text_sign_ip_btn(self):
        description = self.home_new_page.txt_description().text
        self.home_new_page.click_product_btn()
        sleep(10)
        product_description = self.first_product_on_the_left_page.txt_product_description().text
        self.assertEqual(description, product_description)

    def test_19_valid_previous_btn(self):
        txt_product_btn = self.home_new_page.txt_product_btn().text
        self.home_new_page.click_previous_btn()
        sleep(5)
        left_corn_product_after = self.home_new_page.txt_product_btn().text
        self.assertNotEqual(txt_product_btn, left_corn_product_after)

    def test_20_valid_next_btn(self):
        left_corn_product = self.home_new_page.txt_product_btn().text
        self.home_new_page.next_btn_click()
        sleep(5)
        left_corn_product_after = self.home_new_page.txt_product_btn().text
        self.assertNotEqual(left_corn_product, left_corn_product_after)

    def test_21_next_button_displayed_previous_not(self):
        self.scroll = self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(5)
        # check if next button is displayed and previous button not
        is_next_btn_display = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, 'next2'))).is_displayed()
        is_previous_btn_display = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, "prev2"))).is_displayed()

        assert is_previous_btn_display == False and is_next_btn_display == True

    def test_22_previous_button_displayed_next_not(self):
        self.scroll = self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(2)
        # Click next button to go to the next image
        next_btn = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.ID, 'next2')))
        next_btn.click()
        sleep(2)
        is_next_btn_display = next_btn.is_displayed()
        is_previous_btn_display = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.ID, "prev2"))).is_displayed()
        # Check if previous button is displayed and next button is not
        assert is_previous_btn_display == True and is_next_btn_display == False

    def test_27_image_bar_r_btn(self):
        # click the right button in the image bar
        self.driver.find_element(By.XPATH, "/html/body/nav/div[2]/div/a[2]").click()
        sleep(1)
        # Check if the first image is not the same as the second image
        image_1 = self.driver.find_element(By.XPATH, "/html/body/nav/div[2]/div/div/div[1]/img").is_displayed()
        image_2 = self.driver.find_element(By.XPATH, "/html/body/nav/div[2]/div/div/div[2]/img").is_displayed()
        self.assertNotEqual(image_1, image_2)

    def test_28_image_bar_l_btn(self):
        self.driver.find_element(By.XPATH, "/html/body/nav/div[2]/div/a[1]").click()
        sleep(1)
        image_1 = self.driver.find_element(By.XPATH, "/html/body/nav/div[2]/div/div/div[1]/img").is_displayed()
        image_3 = self.driver.find_element(By.XPATH, "/html/body/nav/div[2]/div/div/div[3]/img").is_displayed()
        self.assertNotEqual(image_1, image_3)

    def test_29_about_as_text(self):
        sleep(5)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(5)
        # Check if the 'about us' text is displayed
        assert self.driver.find_element(By.XPATH, '/html/body/div[6]/div/div[1]').is_displayed()

    def test_30_get_in_touch_text(self):
        sleep(5)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(5)
        # Check if the 'get in touch' text is displayed
        assert self.driver.find_element(By.XPATH, '/html/body/div[6]/div/div[2]').is_displayed()