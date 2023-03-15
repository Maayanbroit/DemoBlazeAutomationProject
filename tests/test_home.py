


from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.setup import WebDriverSetup
from selenium.webdriver.common.by import By
from time import sleep


class TestOH(WebDriverSetup):


    def test_1_valid_text_home_btn(self):
        button = self.home_new_page.txt_home_btn()
        button_text = button.text
        self.assertEqual(button_text, "Home")

    def test_2_valid_text_contact_btn(self):
        button = self.home_new_page.txt_contact_btn()
        button_text = button.text
        self.assertEqual(button_text, "Contact")

    def test_3_valid_text_about_us_btn(self):
        button = self.home_new_page.txt_about_us_btn()
        button_text = button.text
        self.assertEqual(button_text, "About us")

    def test_4_valid_text_cart_btn(self):
        button = self.home_new_page.txt_cart_btn()
        button_text = button.text
        self.assertEqual(button_text, "Cart")

    def test_5_valid_text_log_in_btn(self):
        # Test if the text of the log in button is correct
        button = self.home_new_page.txt_log_in_btn()
        button_text = button.text
        expected_text = 'Log in'
        self.assertEqual(button_text, expected_text)

    def test_6_valid_text_sign_up_btn(self):
        button = self.home_new_page.txt_sign_up_btn()
        button_text = button.text
        self.assertEqual(button_text, "Sign up")

    def test_7_click_Home_btn(self):
        self.home_new_page.click_home()
        sleep(2)
        # Check if the current URL is correct
        assert self.driver.current_url == "https://www.demoblaze.com/index.html"

    def test_8_click_Contact_btn(self):
        self.home_new_page.click_Contact()
        sleep(2)
        # Check if the contact popup is displayed
        assert self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div").is_displayed()

    def test_9_click_About_us_btn(self):
        self.home_new_page.click_About_us()
        sleep(2)
        # Check if the about us popup is displayed
        assert self.driver.find_element(By.XPATH, "/html/body/div[4]/div/div").is_displayed()

    def test_10_click_Cart_bnt(self):
        self.home_new_page.click_Cart()
        sleep(2)
        assert self.driver.current_url == "https://www.demoblaze.com/cart.html"

    def test_11_click_Log_in_btn(self):
        self.home_new_page.click_Login()
        sleep(2)
        assert self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div").is_displayed()

    def test_12_click_Sign_up_btn(self):
        self.home_new_page.click_Sign_up()
        sleep(2)
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
        external_title = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/div[5]/div/div[2]/div/div[1]/div/div/p')))
        external_title_text = external_title.text
        external_btn = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="tbodyid"]/div[1]/div/div/h4/a')))
        external_btn.click()
        inner_title = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/div[5]/div/div[2]/div[1]/div/div/p')))
        inner_title_text = inner_title.text
        self.assertEqual(external_title_text, inner_title_text)

    def test_19_valid_previous_btn(self):
        left_corn_product = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[5]/div/div[2]/div/div[1]/div/div/h4/a")))
        left_corn_product_text = left_corn_product.text
        prev_btn = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/div[5]/div/div[2]/form/ul/li[1]/button')))
        prev_btn.click()
        sleep(5)
        left_corn_product_after = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/div[5]/div/div[2]/div/div[1]/div/div/h4/a')))
        left_corn_product_after_text = left_corn_product_after.text
        self.assertNotEqual(left_corn_product_text, left_corn_product_after_text)

    def test_20_valid_next_btn(self):
        left_corn_product = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[5]/div/div[2]/div/div[1]/div/div/h4/a")))
        left_corn_product_text = left_corn_product.text
        next_btn = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/div[5]/div/div[2]/form/ul/li[2]/button')))
        next_btn.click()
        sleep(5)
        left_corn_product_after = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/div[5]/div/div[2]/div/div[1]/div/div/h4/a')))
        left_corn_product_after_text = left_corn_product_after.text
        self.assertNotEqual(left_corn_product_text, left_corn_product_after_text)

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