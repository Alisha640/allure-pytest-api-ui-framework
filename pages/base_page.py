from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)
        self.short_wait = WebDriverWait(driver, 5)

    def wait_for_element(self, locator):
        # element exists in DOM AND is visible
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_for_clickable(self, locator):
        # element exists and is interactable
        return self.wait.until(EC.element_to_be_clickable(locator))

    def wait_for_all(self, locator):
        # multiple same elements — returns list
        return self.wait.until(EC.visibility_of_all_elements_located(locator))

    def wait_for_presence(self, locator):
        # element exists in DOM but may be hidden
        return self.wait.until(EC.presence_of_element_located(locator))

    def wait_for_url_contains(self, text):
        return self.wait.until(EC.url_contains(text))

    def wait_for_given_text_in_element(self, locator, giventext):
        self.wait.until(EC.text_to_be_present_in_element(locator, giventext))
        return self.driver.find_element(*locator).text

    def wait_for_alert(self):
        # JS alerts return an object — use .accept(), .dismiss(), .send_keys()
        return self.wait.until(EC.alert_is_present())

    def is_element_visible(self, locator):
        # returns True/False — use for optional elements
        try:
            self.short_wait.until(EC.visibility_of_element_located(locator))
            return True
        except:
            return False

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def safe_click(self, locator):
        # tries normal click first, falls back to JS click if intercepted
        try:
            self.wait_for_clickable(locator).click()
        except:
            element = self.wait_for_element(locator)
            self.driver.execute_script("arguments[0].click();", element)

    def take_screenshot(self):
        return self.driver.get_screenshot_as_png()