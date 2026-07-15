from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class DynamicPage(BasePage):
    HELLO_WORLD_TEXT = (By.CSS_SELECTOR, "div#finish h4")
    LOADING_BAR_DISPLAY = (By.ID, "loading")
    START_BTN = (By.CSS_SELECTOR, "div#start button")
    NAV_ITEMS = (By.XPATH, "//div[@class='example']/ul/li")
    CHECKBOXES = (By.XPATH, "//form[@id='checkboxes']/input")

    def click_start(self):
        self.wait_for_clickable(self.START_BTN).click()
        self.wait_for_element(self.LOADING_BAR_DISPLAY)

    def get_hello_world_text(self):
        return self.wait_for_element(self.HELLO_WORLD_TEXT).text

    def get_nav_items_count(self):
        return len(self.wait_for_all(self.NAV_ITEMS))

    def refresh_and_wait(self):
        self.driver.refresh()
        self.wait_for_element(self.NAV_ITEMS)

    def click_checkbox(self, index):
        checkbox = self.wait_for_all(self.CHECKBOXES)
        checkbox[index].click()

    def is_checked(self, index):
        checkbox = self.wait_for_all(self.CHECKBOXES)
        return checkbox[index].is_selected()