from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class HoverPage(BasePage):
    FIRST_IMG = (By.XPATH, "//div[@class='example']/*[3]/img")
    FIRST_IMG_CAPTION = (By.XPATH, "//div[@class='example']/div[1]/div/h5")

    def get_first_image(self):
        return self.wait_for_element(self.FIRST_IMG)

    def get_first_image_cap(self):
        return self.wait_for_element(self.FIRST_IMG_CAPTION).text