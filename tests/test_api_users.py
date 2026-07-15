import pytest
import allure
import requests
from data_helpers.csv_reader import get_api_csv_data
from config import MY_KEY, USERS_LIST_URL, SINGLE_USER_URL, NONEXISTENT_USER_URL, CREATE_USER_URL, DELETE_USER_URL, UPDATE_USER_URL, API_BASE_URL

# made api_request() helper as the API call was taking too long or was not reachable at that moment
# Python/requests raised a timeout/connection related err because of that the test failed
@pytest.mark.api
@allure.title("Get Paginated List of Users")
@allure.description("Verify that the system returns a 200 OK status and a list containing valid user objects with required fields.")
@allure.severity(allure.severity_level.NORMAL)
def test_get_users_list(api_request):
    headers = {"x-api-key": MY_KEY}
    response = api_request("get", USERS_LIST_URL, headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert len(data["data"]) > 0
    for user in data["data"]:
        assert "id" in user
        assert "email" in user
        assert "first_name" in user

@pytest.mark.api
@pytest.mark.smoke
@allure.title("Get Single User Profile by ID")
@allure.description("Verify that fetching a specific user profile by ID returns a 200 OK status and the correct user data fields.")
@allure.severity(allure.severity_level.CRITICAL)
def test_get_single_user(api_request):
    headers = {"x-api-key": MY_KEY}
    response = api_request("get", SINGLE_USER_URL, headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert data["data"]["id"] == 2
    assert "@" in data["data"]["email"]

@pytest.mark.api
@allure.title("Get User Profile - Nonexistent ID")
@allure.description("Verify that searching for a user ID that does not exist in the database correctly returns a 404 Not Found error.")
@allure.severity(allure.severity_level.NORMAL)
def test_get_nonexistent_user(api_request):
    headers = {"x-api-key": MY_KEY}
    response = api_request("get", NONEXISTENT_USER_URL, headers=headers)
    assert response.status_code == 404

@pytest.mark.api
@pytest.mark.smoke
@allure.title("Create New User")
@allure.description("Verify that submitting valid user information successfully triggers user creation with a 201 Created status and returns a valid ID.")
@allure.severity(allure.severity_level.CRITICAL)
def test_create_user():
    headers = {"x-api-key": MY_KEY}
    # payload:
    user = {
        "name": "Alice",
        "job": "FrontEnd Engineer"
    }
    response = requests.post(CREATE_USER_URL, headers=headers, json=user)
    assert response.status_code == 201
    data = response.json()
    assert "id" in data
    assert data["name"] == user["name"]
    # on postman the post data don't show up in res as ReqRes is a simulated playground that has hardcoded list of default users so it doesn't add Alice unlike real backend.

@pytest.mark.api
@allure.title("Update Existing User Profile")
@allure.description("Verify that an existing user's profile can be updated via a PUT request and returns a 200 OK status.")
@allure.severity(allure.severity_level.NORMAL)
def test_update_user():
    headers = {"x-api-key": MY_KEY}
    user = {
        "job": "Doctor"
    }
    response = requests.put(UPDATE_USER_URL, headers=headers, json=user)
    assert response.status_code == 200

@pytest.mark.api
@allure.title("Delete User Profile")
@allure.description("Verify that an existing user profile can be removed from the system and returns a 204 No Content status.")
@allure.severity(allure.severity_level.CRITICAL)
def test_delete_user():
    headers = {"x-api-key": MY_KEY}
    response = requests.delete(DELETE_USER_URL, headers=headers)
    assert response.status_code == 204

@pytest.mark.api
@allure.title("Data-Driven API Test: {method} {endpoint}")
@allure.description("Execute data-driven validation across multiple API endpoints using test parameters extracted from a CSV data source.")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize("endpoint,method,payload,expected_status", get_api_csv_data())
def test_api_from_csv(api_request,endpoint,method,payload,expected_status):
    headers = {"x-api-key": MY_KEY}
    url = API_BASE_URL + endpoint
    if method == "GET":
        response = api_request("get", url, headers=headers)
    elif method == "POST":
        response = api_request("post", url, headers=headers, json=payload)
    assert response.status_code == expected_status
