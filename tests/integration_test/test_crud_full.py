# here we write the test cases for full CRUD Operation

from src.constants.api_constants import APIConstants
from src.helpers.api_requests_wrapper import post_request, put_request
from src.helpers.common_verification import verify_response_key_should_not_be_none, verify_http_status_code
from src.helpers.payload_manager import payload_create_booking, payload_create_token, payload_update_booking
from src.helpers.utils import common_headers_json


class TestCreateBooking(object):
    def test_create_token(self):
        response = post_request(url=APIConstants.create_token(), auth=None,
                                headers=common_headers_json(),
                                payload=payload_create_token(),
                                in_json=False)
        verify_http_status_code(response, 200)
        token = response.json()["token"]
        print("This is your token :", token)
        verify_response_key_should_not_be_none(token)
        return token

    def test_create_booking(self):
        # we need urls, headers, payloads
        response = post_request(url=APIConstants.url_create_booking(), auth=None, headers=common_headers_json()
                                , payload=payload_create_booking(), in_json=False)
        print(response)
        bookingid = response.json()["bookingid"]
        print(bookingid)
        verify_response_key_should_not_be_none(response.json()["bookingid"])
        verify_http_status_code(response, 200)
        return bookingid

    def test_update_booking(self):  # to update we need booking ID and token
        token = "9299bfff56ad0d1"
        put_url = APIConstants.url_create_booking() + "/881"
        auth = ("admin", "password123")
        response = put_request(url=put_url, auth=auth, headers=common_headers_json()
                               , payload=payload_update_booking(), in_json=False)
        print(response) 

    def test_delete_booking(self):  # to update we need booking ID and token
        pass
