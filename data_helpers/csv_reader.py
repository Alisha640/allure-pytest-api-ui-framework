import csv
import os
import pytest
import requests
import json
from config import LOGIN_USERNAME

# loading the CSV data into a list of tuples to match parametrize syntax
def get_ui_csv_data():
    data = []
    # os.path ensures it finds the file regardless of from where we run test
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    csv_path = os.path.join(base_dir, 'test_data', 'login_data.csv')
    with open(csv_path, mode ='r') as file:
    # DictReader reads the first row as header nd rest ones as dictionary
        reader = csv.DictReader(file)
        for row in reader:
            # arranged row data in tuple form
            row_tuple = ((row['username'], row['password'], row['expected_text'], row['expected_result']))
            if row['username'] ==  LOGIN_USERNAME:
                data.append(pytest.param(*row_tuple, marks=pytest.mark.smoke))
            else:
                # data.append() places the tuple data in the list- it can alse covert data into tuple form
                data.append(row_tuple)
    return data 

def get_api_csv_data():
    data = []
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    csv_path = os.path.join(base_dir, 'test_data', 'api_data.csv')
    with open(csv_path, mode='r') as file:
        reader = csv.DictReader(file)
        # row looks like this; {"endpoint": "/users/1", "method": "GET", "payload": "", "expected_status": "200"}
        for row in reader:
            payload = json.loads(row['payload']) if row['payload'] else None
            # json.loads() converts json string to python dict
            data.append((
                row['endpoint'],
                row['method'],
                payload,
                int(row['expected_status'])
                # CSV gives string nd we need integer for comparison
            ))
    return data