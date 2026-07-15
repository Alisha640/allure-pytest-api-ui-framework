import pytest
import allure
import requests
from config import MY_KEY, LOGIN_URL, REGISTER_URL, REQRES_EMAIL, REQRES_PASSWORD, API_REGISTER_EMAIL, API_REGISTER_PASSWORD

@pytest.mark.api 
@pytest.mark.smoke
@allure.title("Successful User Login via API")
@allure.description("Verify that a registered user can successfully log in with valid credentials and receive an authentication token.")
@allure.severity(allure.severity_level.BLOCKER)
def test_successful_login(api_request):
    headers = {"x-api-key": MY_KEY}
    payload = {
        "email": REQRES_EMAIL,
        "password": REQRES_PASSWORD
    }
    response = api_request("post", LOGIN_URL, headers=headers, json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "token" in data

@pytest.mark.api 
@pytest.mark.smoke
@allure.title("Failed User Login - Missing Password")
@allure.description("Verify that logging in without providing a password fails with a 400 Bad Request and returns an error message.")
@allure.severity(allure.severity_level.CRITICAL)
def test_failed_login(api_request):
    headers = {"x-api-key": MY_KEY}
    payload = {
        "email": REQRES_EMAIL
    }
    response = api_request("post", LOGIN_URL, headers=headers, json=payload)
    assert response.status_code == 400
    data = response.json()
    assert "error" in data

@pytest.mark.api 
@pytest.mark.smoke
@allure.title("Successful User Registration via API")
@allure.description("Verify that a new user can successfully register with valid email and password, returning an ID and token.")
@allure.severity(allure.severity_level.BLOCKER)
def test_successful_register(api_request):
    headers = {"x-api-key": MY_KEY}
    payload = {
        "email": API_REGISTER_EMAIL,
        "password": API_REGISTER_PASSWORD
    }
    response = api_request("post", REGISTER_URL, headers=headers, json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "token" in data
    assert "id" in data

@pytest.mark.api 
@pytest.mark.smoke
@allure.title("Failed User Registration - Missing Password")
@allure.description("Verify that user registration fails with a 400 Bad Request when the password payload is missing.")
@allure.severity(allure.severity_level.CRITICAL)
def test_failed_register(api_request):
    headers = {"x-api-key": MY_KEY}
    payload = {
        "email": API_REGISTER_EMAIL
    }
    response = api_request("post", REGISTER_URL, headers=headers, json=payload)
    assert response.status_code == 400
    data = response.json()
    assert "error" in data