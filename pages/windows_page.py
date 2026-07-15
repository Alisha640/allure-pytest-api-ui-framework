from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class WindowsPage(BasePage):
    CLICK_HERE_LINK = (By.XPATH, "//a[@href='/windows/new']")
    NEXT_PAGE_HEADING = (By.CSS_SELECTOR, "div.example h3")
    MAIN_PAGE_CONTENT = (By.CSS_SELECTOR, "html.no-js")

    def click_here_link(self):
        self.wait_for_clickable(self.CLICK_HERE_LINK).click()
        self.wait.until(EC.number_of_windows_to_be(2))

    def switch_to_second_tab(self, current_tab):
        for window_handle in self.driver.window_handles:
            if window_handle != current_tab:
                self.driver.switch_to.window(window_handle)
                break
    def close_and_return(self, original_tab):
        self.driver.close()
        self.driver.switch_to.window(original_tab)
        
    def verify_second_tab_heading(self):
        return self.wait_for_element(self.NEXT_PAGE_HEADING).text

    def get_tab_one_content(self):
        return self.wait_for_element(self.MAIN_PAGE_CONTENT).text