
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.setup import WebDriverSetup
from selenium.webdriver.common.by import By

class TestOH(WebDriverSetup):


    def test_38_About_us_video(self):
        self.about_us_page.click_About_us()
        self.about_us_page.click_play_video()
        # Check if the video in the about us popup window is enabled
        assert self.driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div[2]/form/div/div/video").is_enabled()

    def test_39_About_us_close(self):
        self.about_us_page.click_About_us()
        self.about_us_page.click_about_us_close()
        # Check if the about us popup window closes
        assert WebDriverWait(self.driver, 5).until(EC.invisibility_of_element_located((By.XPATH, "/html/body/div[4]/div/div")))
