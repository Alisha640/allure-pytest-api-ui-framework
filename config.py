from dotenv import load_dotenv
import os

load_dotenv()

# credentials from .env
LOGIN_USERNAME = os.getenv('LOGIN_USERNAME')
LOGIN_PASSWORD = os.getenv('LOGIN_PASSWORD')
MY_KEY = os.getenv('MY_KEY')
REQRES_EMAIL = os.getenv('REQRES_EMAIL')
REQRES_PASSWORD = os.getenv('REQRES_PASSWORD')
API_REGISTER_EMAIL = os.getenv('API_REGISTER_EMAIL')
API_REGISTER_PASSWORD = os.getenv('API_REGISTER_PASSWORD')

# base URLs
BASE_URL = 'https://the-internet.herokuapp.com'
API_BASE_URL = 'https://reqres.in/api'

# UI page URLs
UI_LOGIN_URL = f'{BASE_URL}/login'
SECURE_URL = f'{BASE_URL}/secure'
DROPDOWN_URL = f'{BASE_URL}/dropdown'
JS_ALERTS_URL = f'{BASE_URL}/javascript_alerts'
WINDOWS_URL = f'{BASE_URL}/windows'
UPLOAD_URL = f'{BASE_URL}/upload'
HOVER_URL = f'{BASE_URL}/hovers'
DYNAMIC_LOADING_URL = f'{BASE_URL}/dynamic_loading/1'
DISAPPEARING_URL = f'{BASE_URL}/disappearing_elements'
CHECKBOXES_URL = f'{BASE_URL}/checkboxes'

# API URLS
USERS_LIST_URL = f'{API_BASE_URL}/users?page=2'
SINGLE_USER_URL = f'{API_BASE_URL}/users/2'
NONEXISTENT_USER_URL = f'{API_BASE_URL}/users/999'
CREATE_USER_URL = f'{API_BASE_URL}/users'
UPDATE_USER_URL = f'{API_BASE_URL}/users/2'
DELETE_USER_URL = f'{API_BASE_URL}/users/2'
LOGIN_URL = f"{API_BASE_URL}/login"
REGISTER_URL = f"{API_BASE_URL}/register"