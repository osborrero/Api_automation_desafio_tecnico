import json
import requests
from src.page.utils.Constants import TestDataBooker
from src.test.suites.utils.Functions import CommonFunctions


class Service:
    @staticmethod
    def get_access_token(payload):
        url = TestDataBooker.url_CreateToken()
        response_service = requests.post(url, data=json.dumps(payload),
                                         headers=TestDataBooker.HEADER)
        response = response_service.json() if response_service.status_code == 200 else response_service.text
        return response['token'], response_service.status_code

    @staticmethod
    def get_bookingIds():
        url = TestDataBooker.url_getBookingIds()
        response_service = requests.get(url)
        response = response_service.json() if response_service.status_code == 200 else response_service.text
        return response, response_service.status_code

    @staticmethod
    def get_bookingId(num):
        url = f"{TestDataBooker.url_getBookingIds()}/{num}"
        response_service = requests.get(url)
        response = response_service.json() if response_service.status_code == 200 else response_service.text
        return response, response_service.status_code

    @staticmethod
    def post_createBooking(payload):
        url = TestDataBooker.url_getBookingIds()
        response_service = requests.post(url, data=json.dumps(payload),
                                         headers=TestDataBooker.HEADER)
        response = response_service.json() if response_service.status_code == 200 else response_service.text
        return response, response_service.status_code

    @staticmethod
    def put_updateBooking(num, payload, token):
        url = f"{TestDataBooker.url_getBookingIds()}/{num}"
        headers_base = TestDataBooker.HEADER_UPDATEBOOKING
        headers_base["Cookie"] += token
        response_service = requests.put(url, data=json.dumps(payload),
                                         headers=headers_base)
        response = response_service.json() if response_service.status_code == 200 else response_service.text
        value = CommonFunctions.validate_data_bookings(response, payload)
        return response, response_service.status_code, value

    @staticmethod
    def pacth_partialUpdateBooking(num, payload, token):
        url = f"{TestDataBooker.url_getBookingIds()}/{num}"
        headers_base = TestDataBooker.HEADER_UPDATEBOOKING
        response_service = requests.patch(url, data=json.dumps(payload),
                                        headers=headers_base)
        response = response_service.json() if response_service.status_code == 200 else response_service.text
        return response, response_service.status_code

    @staticmethod
    def delete_Booking(num, token):
        url = f"{TestDataBooker.url_getBookingIds()}/{num}"
        headers_base = TestDataBooker.HEADER_DELETEBOOKING
        headers_base["Cookie"] += token
        response_service = requests.delete(url, headers=headers_base, data=None)
        response = response_service.json() if response_service.status_code == 200 else response_service.text
        return response, response_service.status_code

    @staticmethod
    def getHealthCheck():
        url = TestDataBooker.url_getHealthCheck()
        response_service = requests.get(url)
        response = response_service.json() if response_service.status_code == 200 else response_service.text
        return response, response_service.status_code
