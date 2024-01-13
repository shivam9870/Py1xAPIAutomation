# Read the Excel or CSV file
# We create a function that takes the value from the Excel/CSV file
# and at the end verify the expected result
# Read the Excel file - library ->> openpyxl
import sys

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


def test_post_create_token():
    # make_request_auth -> Run this func, Rows that we have in excel
    file_path = "C:/Users/Shivam/PycharmProjects/Py1xAPIAutomation/tests/datadriventesting/testdata_ddt.xlsx"
    credentials = read_credential_from_excel(file_path)

    for user_cred in credentials:
        username = user_cred["username"]
        password = user_cred["password"]
        print(username, password)
        response = make_request_auth(username, password)
        print(response)
        # Here you can also write the logic for negative and positive
        assert response.status_code == 200
