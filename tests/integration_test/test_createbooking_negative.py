from src.constants.api_constants import APIConstants
from src.helpers.api_requests_wrapper import post_request
from src.helpers.common_verification import verify_http_status_code
from src.helpers.utils import common_headers_json


class TestCreateBooking(object):
    def test_create_booking_tc1(self):
        # we need urls, headers, payloads
        response = post_request(url=APIConstants.url_create_booking(), auth=None, headers=common_headers_json()
                                , payload={}, in_json=False)
        verify_http_status_code(response, 500)

    def test_create_booking_tc2(self):
        # we need urls, headers, payloads
        response = post_request(url=APIConstants.url_create_booking(), auth=None, headers=common_headers_json()
                                , payload=None, in_json=False)
        verify_http_status_code(response, 500)  # giving the payload as None

    def test_create_booking_tc3(self):
        # we need urls, headers, payloads
        response = post_request(url=APIConstants.url_create_booking(), auth=None, headers=common_headers_json()
                                , payload="this is a text", in_json=False)
        verify_http_status_code(response, 500)  # giving the text file as a payload

    def test_create_booking_tc4(self):
        # we need urls, headers, payloads
        response = post_request(url=APIConstants.url_create_booking(), auth=None, headers=common_headers_json()
                                , payload="@@@@", in_json=False)
        verify_http_status_code(response, 500)  # giving special value in the payload

    # same like that we can write many negative test cases.
    # exp= here any junior tester write negative as well as positive test_cases. with the help of source folder.
