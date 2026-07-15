import sys
import os
import allure
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from pages.dynamic_page import DynamicPage
from config import DYNAMIC_LOADING_URL, DISAPPEARING_URL, CHECKBOXES_URL

@pytest.mark.ui
@pytest.mark.smoke
@allure.title("Verify Dynamic Loading Animations")
@allure.description("Validates that elements correctly appear on the webpage once the loading animation is completed.")
@allure.severity(allure.severity_level.CRITICAL)
def test_dynamic_loading(driver):
    driver.get(DYNAMIC_LOADING_URL) 
    dynamic_page = DynamicPage(driver)
    dynamic_page.click_start()
    assert 'Hello World!' in dynamic_page.get_hello_world_text()

@pytest.mark.ui
@pytest.mark.regression
@allure.title("Verify Stability of Disappearing Elements")
@allure.description("Validates that the UI layout elements persist and remain stable after refreshing the page.")
@allure.severity(allure.severity_level.NORMAL)
def test_disappearing_elements(driver):
    driver.get(DISAPPEARING_URL) 
    dynamic_page = DynamicPage(driver)
    assert dynamic_page.get_nav_items_count() > 0
    dynamic_page.refresh_and_wait()
    assert dynamic_page.get_nav_items_count() > 0

@pytest.mark.ui
@pytest.mark.smoke
@allure.title("Verify Checkbox States and Toggling")
@allure.description("Validates that is_selected() accurately returns True for a checked state and False for unchecked states.")
@allure.severity(allure.severity_level.NORMAL)
def test_checkboxes(driver):
    driver.get(CHECKBOXES_URL) 
    dynamic_page = DynamicPage(driver)
    assert not dynamic_page.is_checked(0)
    assert dynamic_page.is_checked(1)
    dynamic_page.click_checkbox(0)
    assert dynamic_page.is_checked(0)
    dynamic_page.click_checkbox(1)
    assert not dynamic_page.is_checked(1)

# Morning standup → py -m pytest -m smoke    # 2 min check
# Before release  → py -m pytest -m regression  # full check