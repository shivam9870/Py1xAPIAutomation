# SOme payloads
import json
from faker import Faker

faker= Faker()

def payload_create_booking():
    payload = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    return payload


def payload_create_booking_dynamic():
    json_payload = {
        "firstname": faker.first_name(),
        "lastname": faker.last_name(),
        "totalprice": faker.random_int(min=100,max=1000),
        "depositpaid": faker.boolean(),
        # "bookingdates": {
        #     "checkin": str(faker.date_between(start_date='-3y',end_date='today')),
        #     "checkout": str(faker.date_between(start_date='today',end_date='+3y'))
        # },
        # above code is only for remember purpose
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": faker.random_element(elements=("Breakfast","Wifi","Parking"))
    }
    return json_payload


def payload_create_token():
    payload = {
        "username": "admin",
        "password": "password123"
    }
    return payload


def payload_update_booking():
    payload = {
        "firstname": "Shivam",
        "lastname": "Shrivastav",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    return payload
