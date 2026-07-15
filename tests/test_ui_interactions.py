import sys
import os
import allure
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from selenium.webdriver.common.action_chains import ActionChains
from pages.dropdown_page import DropdownPage
from pages.alerts_page import AlertsPage
from pages.windows_page import WindowsPage
from pages.upload_page import UploadPage
from pages.hover_page import HoverPage
from config import DROPDOWN_URL, JS_ALERTS_URL, WINDOWS_URL, UPLOAD_URL, HOVER_URL

@pytest.mark.ui
@pytest.mark.smoke
@allure.title("Verify Dropdown Option Selection")
@allure.description("Validates that selecting an option from a select dropdown correctly updates its active selection state.")
@allure.severity(allure.severity_level.NORMAL)
def test_dropdown(driver):
    driver.get(DROPDOWN_URL)
    dropdown_page = DropdownPage(driver)
    dropdown_page.select_option("Option 1")
    assert dropdown_page.is_selected('1') is True

@pytest.mark.ui
@pytest.mark.regression
@allure.title("Verify JavaScript Alert Handling")
@allure.description("Validates that browser alert windows are handled correctly using accept, dismiss, and prompt messaging actions.")
@allure.severity(allure.severity_level.CRITICAL)
def test_javascript_alerts(driver):
    driver.get(JS_ALERTS_URL)
    alerts_page = AlertsPage(driver)
    alerts_page.click_btn('Click for JS Alert')
    alerts_page.ok_alert()
    assert "You successfully clicked an alert" in alerts_page.get_result()
    alerts_page.click_btn('Click for JS Confirm')
    alerts_page.cancel_alert()
    assert "You clicked: Cancel" in alerts_page.get_result()
    alerts_page.click_btn('Click for JS Prompt')
    alerts_page.prompt_alert("hello")
    alerts_page.ok_alert()
    assert "You entered: hello" in alerts_page.get_result()

@pytest.mark.ui
@pytest.mark.regression
@allure.title("Verify Multiple Window and Tab Handling")
@allure.description("Validates switching browser window handles smoothly to verify child tabs and safely returning to the main page.")
@allure.severity(allure.severity_level.CRITICAL)
def test_multiple_windows(driver):
    driver.get(WINDOWS_URL)
    windows_page = WindowsPage(driver)
    tab_one = driver.current_window_handle
    windows_page.click_here_link()
    windows_page.switch_to_second_tab(tab_one)
    assert "New Window" in windows_page.verify_second_tab_heading()
    windows_page.close_and_return(tab_one)
    assert windows_page.get_tab_one_content()

@pytest.mark.ui
@pytest.mark.regression
@allure.title("Verify File Upload via Input Field")
@allure.description("Validates that a created file is successfully submitted to the server without opening browser dialog windows.")
@allure.severity(allure.severity_level.NORMAL)
def test_file_upload(driver):
    driver.get(UPLOAD_URL)
    upload_page = UploadPage(driver)
    new_file = "test_file.txt"
    with open(new_file, mode='w') as file:
        file.write("QA Automation- Mock Project")
    file_adress = os.path.abspath(new_file)
    upload_page.choose_file(file_adress)
    upload_page.click_upload_btn()
    assert "File Uploaded!" in upload_page.get_sucess_msg()
    assert upload_page.file_name_appeared() == new_file

@pytest.mark.ui
@pytest.mark.regression
@allure.title("Verify Hidden Tooltip/Caption Display on Hover")
@allure.description("Validates that simulating hover actions using Selenium ActionChains accurately reveals hidden image captions.")
@allure.severity(allure.severity_level.MINOR)
def test_hover_interaction(driver):
    driver.get(HOVER_URL)
    hover_page = HoverPage(driver)
    actions = ActionChains(driver)
    actions.move_to_element(hover_page.get_first_image()).perform()
    assert "name: user1" in hover_page.get_first_image_cap()


