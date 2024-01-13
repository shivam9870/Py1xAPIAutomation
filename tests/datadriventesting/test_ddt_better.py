# Read the Excel or CSV file
# We create a function that takes the value from the Excel/CSV file
# and at the end verify the expected result
# Read the Excel file - library ->> openpyxl
import sys

import pytest

sys.path.append(r'C:\Users\Shivam\PycharmProjects\Py1xAPIAutomation')  # Adjust the path as needed

import openpyxl
import requests

from src.helpers.utils import common_headers_json


# Read a file and add into a [array]


def read_credential_from_excel(file_path):
    credentials = []
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active
    for row in sheet.iter_rows(min_row=2, values_only=True):
        username, password = row
        credentials.append({"username": username, "password": password})
    return credentials


def make_request_auth(username, password):
    payload = {
        "username": username,
        "password": password
    }

    response = requests.post(url="https://restful-booker.herokuapp.com/auth", headers=common_headers_json(),
                             json=payload)
    return response

@pytest.mark.parametrize("user_cred",read_credential_from_excel("C:/Users/Shivam/PycharmProjects/Py1xAPIAutomation/tests/datadriventesting/testdata_ddt.xlsx"))
def test_post_create_token(user_cred):
    username = user_cred["username"]
    password = user_cred["password"]
    print(username, password)
    response = make_request_auth(username, password)
    print(response)
