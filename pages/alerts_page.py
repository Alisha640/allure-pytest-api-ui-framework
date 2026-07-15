from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class AlertsPage(BasePage):
    RESULT_TEXT = (By.ID, "result")

    def click_btn(self, text):
        self.wait_for_clickable((By.XPATH, f"//button[text()='{text}']")).click()

    def ok_alert(self):
        self.wait_for_alert().accept()

    def cancel_alert(self):
        self.wait_for_alert().dismiss()

    def prompt_alert(self, prompt):
        self.wait_for_alert().send_keys(prompt)

    def get_result(self):
        return self.wait_for_element(self.RESULT_TEXT).text