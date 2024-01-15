# here we write the test cases for create booking
import json

import pytest

from src.constants.api_constants import APIConstants
from src.helpers.api_requests_wrapper import post_request
from src.helpers.common_verification import verify_response_key_should_not_be_none, verify_http_status_code
from src.helpers.payload_manager import payload_create_booking
from src.helpers.utils import common_headers_json

from jsonschema import validate
from jsonschema.exceptions import ValidationError


class TestCreateBooking(object):

    def load_schema(self,schema_file):
        with open(schema_file,'r') as file:
            return json.load(file)

    def test_create_bookingwith_jsonschema(self):
        # we need urls, headers, payloads
        response = post_request(url=APIConstants.url_create_booking(), auth=None, headers=common_headers_json()
                                , payload=payload_create_booking(), in_json=False)
        print(response)
        bookingid = response.json()["bookingid"]
        print(bookingid)
        verify_response_key_should_not_be_none(response.json()["bookingid"])
        verify_http_status_code(response, 200)
        response_json = response.json()

        schema = self.load_schema("C:/Users/Shivam/PycharmProjects/Py1xAPIAutomation/tests/json_schema/schema.json")

        try:
            validate(instance=response_json, schema=schema)
        except ValidationError as e:
            print(e.message)
