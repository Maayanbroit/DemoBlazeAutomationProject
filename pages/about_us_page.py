
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.about_us_locators import About_As_Locators

class About_As_page:

    def __init__(self, driver):
        self.driver = driver


    def click_About_us(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, About_As_Locators.about_us_btn))).click()
        WebDriverWait(self.driver, 10)

    def click_play_video(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, About_As_Locators.play_video_btn))).click()
        WebDriverWait(self.driver, 10)

    def click_about_us_close(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, About_As_Locators.about_us_close_btn))).click()
        WebDriverWait(self.driver, 10)

    #assert tests 38-39:
    def video_enabled(self):
        x = self.driver.find_element(By.XPATH, About_As_Locators.video_enabled).is_enabled()
        return x
    def about_us_pop_up_close(self):
        x = WebDriverWait(self.driver, 5).until(EC.invisibility_of_element_located((By.XPATH, About_As_Locators.about_us_pop_up)))
        return x