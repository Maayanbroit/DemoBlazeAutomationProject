
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators1.about_us_locators import About_As_Locators

class About_As_page:

    def __init__(self, driver):
        self.driver = driver


    def click_About_us(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, About_As_Locators.about_us_btn))).click()


    def click_play_video(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, About_As_Locators.play_video_btn))).click()

    def click_about_us_close(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, About_As_Locators.about_us_close_btn))).click()
