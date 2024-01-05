# To make the PUT, PATCH, POST, DELETE
# HTTP Method - Generic function
import json

import requests
from requests import Response


def get_request(url, auth, in_json):
    response = requests.get(url=url, auth=auth)
    if in_json is True:
        return response.json()
    return response


def post_request(url, auth, in_json, headers, payload):
    post_response = requests.post(url=url, headers=headers, auth=auth, data=json.dumps(payload))
    # json.dumps= whatever is payload it gives you in a json format. like a converter to JSON Format
    if in_json is True:
        return post_response.json()
    return post_response


def patch_request(url, auth, in_json, headers, payload):
    patch_request_data = requests.patch(url=url, headers=headers, auth=auth, data=json.dumps(payload))
    # json.dumps= whatever is payload it gives you in a json format. like a converter to JSON Format
    if in_json is True:
        return patch_request_data.json()
    return patch_request_data


def put_request(url, auth, in_json, headers, payload):
    put_request_data = requests.put(url=url, headers=headers, auth=auth, data=json.dumps(payload))
    # json.dumps= whatever is payload it gives you in a json format. like a converter to JSON Format
    if in_json is True:
        return put_request_data.json()
    return put_request_data


def delete_request(url, auth, in_json, headers, payload):
    delete_request_data = requests.delete(url=url, headers=headers, auth=auth, data=json.dumps(payload))
    # json.dumps= whatever is payload it gives you in a json format. like a converter to JSON Format
    if in_json is True:
        return delete_request_data.json()
    return delete_request_data
