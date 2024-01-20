import copy
import json
import os

from src.page.utils.Constants import TestDataBooker



class CommonFunctions:

    @staticmethod
    def get_configuration_json():
        with open(TestDataBooker.data_input, encoding="utf-8") as json_file:
            payload = json.load(json_file)
        return copy.deepcopy(payload['MOCK_BOOKER'])


    @staticmethod
    def number_of_records_of_bookingid(booking_ids_list):
        number_booking_ids = len(booking_ids_list)
        return number_booking_ids

    @staticmethod
    def validate_data_bookings(data_booking_send, response_date):
        value = data_booking_send == response_date
        return value