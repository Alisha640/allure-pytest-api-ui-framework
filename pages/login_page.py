from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class LoginPage(BasePage):
    USERNAME_FIELD = (By.NAME, "username")
    PASSWORD_FIELD = (By.NAME, "password")
    LOGIN_BTN = (By.CLASS_NAME, "radius")
    FLASH_MSG = (By.ID, "flash")
    LOGOUT_BTN = (By.CSS_SELECTOR, "a.button.secondary.radius")

    def enter_username(self, username):
        self.wait_for_element(self.USERNAME_FIELD).send_keys(username)

    def enter_password(self, password):
        self.wait_for_element(self.PASSWORD_FIELD).send_keys(password)

    def click_login(self):
        self.wait_for_clickable(self.LOGIN_BTN).click()

    def get_msg(self):
        return self.wait_for_element(self.FLASH_MSG).text

    def click_logout(self):
        self.wait_for_clickable(self.LOGOUT_BTN).click()