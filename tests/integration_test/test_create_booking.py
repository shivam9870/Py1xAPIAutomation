# here we write the test cases for create booking
import pytest

from src.constants.api_constants import APIConstants
from src.helpers.api_requests_wrapper import post_request
from src.helpers.common_verification import verify_response_key_should_not_be_none, verify_http_status_code
from src.helpers.payload_manager import *
from src.helpers.utils import common_headers_json


class TestCreateBooking(object):
    @pytest.mark.positive
    def test_create_booking_tc1(self):
        # we need urls, headers, payloads
        response = post_request(url=APIConstants.url_create_booking(), auth=None, headers=common_headers_json()
                                , payload=payload_create_booking(), in_json=False)
        print(response)
        bookingid = response.json()["bookingid"]
        print(bookingid)
        verify_response_key_should_not_be_none(response.json()["bookingid"])
        verify_http_status_code(response, 200)

    @pytest.mark.nagative
    def test_create_booking_tc2(self):
        # we need urls, headers, payloads
        response = post_request(url=APIConstants.url_create_booking(), auth=None, headers=common_headers_json()
                                , payload={}, in_json=False)
        verify_http_status_code(response, 500)

# to update the dict value use:
# payload.update({"firstname": "shivam","lastname": "shrivastav"})
# you can use multiple key value pair
