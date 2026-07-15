import pytest
import os
import allure
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

def pytest_addoption(parser):
    parser.addoption('--browser', default='chrome', help='Browser: chrome or firefox')
    parser.addoption('--headless', action='store_true', help='Run headless')

@pytest.fixture
def api_request():
    def _request(method, url, **kwargs):
        try:
            # wait for the api res for 10 secs
            response = requests.request(method, url, timeout=10, **kwargs)
            return response
        except requests.exceptions.RequestException as exc:
            # catches issues like no interner,DNS issue etc
            pytest.skip(f"API endpoint unavailable: {exc}")
            # nd skips the test due to unavailability of api instead of crrashing the whole suite
    return _request


@pytest.fixture
def driver(request):
    browser = request.config.getoption('--browser')
    headless = request.config.getoption('--headless')

    if browser == 'chrome':
        options = ChromeOptions()
        options.add_experimental_option("prefs", {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.default_content_setting_values.notifications": 2
        })
        options.add_argument("--incognito")
        options.add_argument("--disable-notifications")
        if headless:
            options.add_argument("--headless")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Chrome(options=options)

    elif browser == 'firefox':
        options = FirefoxOptions()
        if headless:
            options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)

    else:
         raise ValueError(f"Unsupported browser: {browser}. Choose 'chrome' or 'firefox'.")
         
    yield driver
    driver.quit()

# autouse=True means fixture applies to every test automatically
@pytest.fixture(autouse=True)
def attach_screenshot_on_failure(request):
    # yield means test runs here, everything after yield runs once the test is completed
    yield
    # only take screenshot if driver fixture was used in this test
    driver = request.node.funcargs.get("driver")
    if driver and request.node.rep_call.failed:
        allure.attach(
            driver.get_screenshot_as_png(),
            name="failure_screenshot",
            attachment_type=allure.attachment_type.PNG
        )

# hookimpl hooks into pytest's internal reporting to make rep_call available
# rep_call.failed is True only if the actual test body failed (not setup/teardown)
# without hookimpl rep_call doesn't exist and ss fixture crashes
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)