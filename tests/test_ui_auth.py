import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
import allure
from pages.login_page import LoginPage
from data_helpers.csv_reader import get_ui_csv_data
from config import UI_LOGIN_URL

@pytest.mark.ui
@allure.title("UI Login Verification: User '{username}' , Expected: {expected_result}")
@allure.description("Validates that successful login shows a success message and an unsuccessful login attempt shows an error message.")
@allure.severity(allure.severity_level.BLOCKER)
@pytest.mark.parametrize("username,password,expected_text,expected_result", get_ui_csv_data())
def test_user_login(driver,username,password,expected_text,expected_result):
    driver.get(UI_LOGIN_URL)
    login_page = LoginPage(driver)
    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_login()
    if expected_result == "success":
        assert "secure area" in login_page.get_msg()
        assert "secure" in driver.current_url
        login_page.click_logout()
        assert "login" in driver.current_url
    else:
        assert expected_text in login_page.get_msg()

# get_ui_csv_data() reads login_data.csv and returns list of tuples
# parametrize unpacks each row as (username, password, expected_text, expected_result)
# CSV driven = non-technical people can add test cases without touching code

# things to think while setting allure.severity() :
# Does it stop money/users from moving forward? (BLOCKER)
# Is it a primary feature or data altering action? (CRITICAL)
# Is it an edge case or a secondary feature? (NORMAL or MINOR)
# Is it a typo, wrong font/color? (TRIVIAL)