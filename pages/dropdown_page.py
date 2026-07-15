from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage

class DropdownPage(BasePage):
    DROPDOWN = (By.ID, "dropdown")

    def select_option(self, text):
        select = Select(self.wait_for_element(self.DROPDOWN))
        select.select_by_visible_text(text)

    def is_selected(self, value):
        option = self.wait_for_element((By.XPATH, f"//option[@value='{value}']"))
        return bool(option.get_attribute("selected"))