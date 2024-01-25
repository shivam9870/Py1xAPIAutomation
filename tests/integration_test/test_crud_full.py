# here we write the test cases for full CRUD Operation

import pytest

from src.constants.api_constants import APIConstants
from src.helpers.api_requests_wrapper import post_request, put_request, delete_request
from src.helpers.common_verification import verify_response_key_should_not_be_none, verify_http_status_code
from src.helpers.payload_manager import *
from src.helpers.utils import common_headers_json


class TestCreateBooking(object):
    @pytest.fixture()
    def create_token(self):
        response = post_request(url=APIConstants.create_token(), auth=None,
                                headers=common_headers_json(),
                                payload=payload_create_token(),
                                in_json=False)
        verify_http_status_code(response, 200)
        token = response.json()["token"]
        print("This is your token :", token)
        verify_response_key_should_not_be_none(token)
        return token

    @pytest.fixture()
    def create_booking(self):
        # we need urls, headers, payloads
        response = post_request(url=APIConstants.url_create_booking(), auth=None, headers=common_headers_json()
                                , payload=payload_create_booking(), in_json=False)
        print(response)
        bookingid = response.json()["bookingid"]
        print(bookingid)
        verify_response_key_should_not_be_none(response.json()["bookingid"])
        verify_http_status_code(response, 200)
        print(bookingid)
        return bookingid

    def test_update_booking(self, create_token, create_booking):  # to update we need booking ID and token
        bookingid = create_booking
        auth = ("admin", "password123")
        put_url = APIConstants.url_create_booking() + "/" + str(bookingid)
        response = put_request(url=put_url, headers=common_headers_json(), auth=auth,
                               payload=payload_update_booking(), in_json=False)
        print(response.json())

    def test_delete_booking(self,create_booking):  # to update we need booking ID and token
        bookingid= create_booking
        auth = ("admin", "password123")
        delete_url= APIConstants.url_create_booking() + "/" + str(bookingid)
        response = delete_request(url=delete_url, auth=auth,
                                  payload=None,headers=common_headers_json(), in_json=False)
