from src.constants.api_constants import APIConstants
import requests


def test_crud():
    url_link = APIConstants.base_url()
    print(url_link)
