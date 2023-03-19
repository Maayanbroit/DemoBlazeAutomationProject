
from utilities.setup import WebDriverSetup


class TestOH(WebDriverSetup):


    def test_38_About_us_video(self):
        self.about_us_page.click_About_us()
        self.about_us_page.click_play_video()
        # Check if the video in the about us popup window is enabled
        assert self.about_us_page.video_enabled()

    def test_39_About_us_close(self):
        self.about_us_page.click_About_us()
        self.about_us_page.click_about_us_close()
        # Check if the about us popup window closes
        assert self.about_us_page.about_us_pop_up_close()
