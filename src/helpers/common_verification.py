# HTTP Status code

def verify_http_status_code(response_data, expect_data):
    assert response_data.status_code == expect_data, "Expected HTTP Status Code" + str(expect_data)


def verify_json_key_is_not_null(key):
    assert key != 0, "Key is not null" + key
    assert key > 0, "Key is greater than zero"


def verify_response_key_should_not_be_none(key):
    assert key is not None  # verify that token is not empty


def verify_response_time():
    pass

# Common Verification
# Headers, HTTP Status code, JSON Schema, Data Verification
