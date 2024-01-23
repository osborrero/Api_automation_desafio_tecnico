import unittest
import copy
from test_junkie.decorators import Suite, test

from src.page.utils.Constants import TestDataBooker
from src.page.utils.LogCustom import logger
from src.test.suites.utils.Functions import CommonFunctions
from src.webService.BookerServices import Service


def custom_skip_function():
    return False


@Suite(feature="RestFul Booker", owner="Integrations YAPE")
class RestfulBooker(unittest.TestCase):
    payload = CommonFunctions.get_configuration_json()

    def run_auth_createToken(self, value):
        payload_access_token = copy.deepcopy(self.payload[value])
        token, status_code = Service.get_access_token(payload_access_token)
        return token, status_code

    def run_booking_Ids(self):
        response, status_code = Service.get_bookingIds()
        number_of_records_of_bookingid = CommonFunctions.number_of_records_of_bookingid(response)
        return number_of_records_of_bookingid, status_code

    def run_createBooking(self, value):
        payload_createBooking = copy.deepcopy(self.payload[value])
        bookingid, status_code = Service.post_createBooking(payload_createBooking)
        return bookingid, status_code

    def run_booking_by_id(self, Booking_id):
        response, status_code = Service.get_bookingId(Booking_id)
        return response, status_code

    def run_updateBooking(self, value, Booking_id, access_token):
        payload_updateBooking = copy.deepcopy(self.payload[value])
        response, status_code, value = Service.put_updateBooking(Booking_id, payload_updateBooking, access_token)
        return response, status_code, value

    def run_partialUpdateBooking(self, value, Booking_id, access_token):
        payload_partialUpdateBooking = copy.deepcopy(self.payload[value])
        response, status_code = Service.pacth_partialUpdateBooking(Booking_id, payload_partialUpdateBooking, access_token)
        return response, status_code, payload_partialUpdateBooking

    def run_delete_Booking(self, Booking_id, access_token):
        response, status_code = Service.delete_Booking(Booking_id, access_token)
        return response, status_code

    def run_getHealthCheck(self):
        response, status_code = Service.getHealthCheck()
        return response, status_code

    @test(skip=custom_skip_function, component="HappyPaths_01", parallelized_parameters=True)
    def GetHealthCheck(self, suite_parameter, parameter):
        logger.info(" @TEST - GetHealthCheck")
        response, status_code = self.run_getHealthCheck()
        self.assertEqual(status_code, 201)
        self.assertEqual(response, 'Created')

    @test(skip=custom_skip_function, component="HappyPaths_02", parallelized_parameters=True)
    def Auth_CreateToken(self, suite_parameter, parameter):
        logger.info(" @TEST - Auth_CreateToken")
        token, status_code = self.run_auth_createToken('Auth-CreateToken')
        self.assertEqual(status_code, 200)
        self.access_token = token

    @test(skip=custom_skip_function, component="HappyPaths_03", parallelized_parameters=True)
    def GetBookingIds(self, suite_parameter, parameter):
        logger.info(" @TEST - GetBookingIds")
        number_of_records_of_bookingid, status_code = self.run_booking_Ids()
        logger.info(f"Se encontraron {number_of_records_of_bookingid} en la respuesta")
        self.assertEqual(status_code, 200)

    @test(skip=custom_skip_function, component="HappyPaths_04", parallelized_parameters=True)
    def CreateBooking(self, suite_parameter, parameter):
        logger.info(" @TEST - CreateBooking")
        response, status_code = self.run_createBooking('CreateBooking')
        self.assertEqual(status_code, 200)
        self.Booking_id = response['bookingid']
        self.Data_booking_send = response['booking']
        logger.info(f"Los datos creados son {response['booking']}")

    @test(skip=custom_skip_function, component="HappyPaths_05", parallelized_parameters=True)
    def GetBookingById(self, suite_parameter, parameter):
        logger.info(" @TEST - GetBookingById")
        response_date, status_code = self.run_booking_by_id(self.Booking_id)
        self.assertEqual(status_code, 200)
        logger.info(f"Los datos del id es {response_date} en la respuesta")
        value = CommonFunctions.validate_data_bookings(self.Data_booking_send, response_date)
        self.assertTrue(value)

    @test(skip=custom_skip_function, component="HappyPaths_06", parallelized_parameters=True)
    def PutUpdateBooking(self, suite_parameter, parameter):
        logger.info(" @TEST - PutUpdateBooking")
        response_date, status_code, value = self.run_updateBooking('UpdateBooking', self.Booking_id, self.access_token)
        logger.info(f"Los datos nuevos son {response_date}")
        self.assertEqual(status_code, 200)
        self.assertTrue(value)

    @test(skip=custom_skip_function, component="HappyPaths_07", parallelized_parameters=True)
    def PatchPartialUpdateBooking(self, suite_parameter, parameter):
        logger.info(" @TEST - PatchPartialUpdateBooking")
        response_date, status_code, payload_partialUpdateBooking = self.run_partialUpdateBooking('PartialUpdateBooking', self.Booking_id, self.access_token)
        logger.info(f"Los datos nuevos son {response_date}")
        self.assertEqual(status_code, 200)
        self.assertDictContainsSubset(payload_partialUpdateBooking, response_date)

    @test(skip=custom_skip_function, component="HappyPaths_08", parallelized_parameters=True)
    def DeleteBooking(self, suite_parameter, parameter):
        logger.info(" @TEST - DeleteBooking")
        response, status_code = self.run_delete_Booking(self.Booking_id, self.access_token)
        self.assertEqual(status_code, 201)
        self.assertEqual(response, 'Created')

    @test(skip=custom_skip_function, component="UnHappyPaths_01", parallelized_parameters=True)
    def DeleteBooking_incorrect_token(self, suite_parameter, parameter):
        logger.info(" @TEST - DeleteBooking_incorrect_token")
        response, status_code = self.run_delete_Booking(self.Booking_id, TestDataBooker.TOKEN_INCORRECT)
        self.assertEqual(status_code, 403)
        self.assertEqual(response, 'Forbidden')

    @test(skip=custom_skip_function, component="UnHappyPaths_02", parallelized_parameters=True)
    def DeleteBooking_incorrect_Booking_id(self, suite_parameter, parameter):
        logger.info(" @TEST - DeleteBooking_incorrect_Booking_id")
        response, status_code = self.run_delete_Booking(f"{self.Booking_id}a", self.access_token)
        self.assertEqual(status_code, 403)
        self.assertEqual(response, 'Forbidden')

    @test(skip=custom_skip_function, component="UnHappyPaths_03", parallelized_parameters=True)
    def GetBookingBy_incorrect_Booking_Id(self, suite_parameter, parameter):
        logger.info(" @TEST - GetBookingBy_incorrect_Booking_Id")
        response, status_code = self.run_booking_by_id(f"{self.Booking_id}a")
        self.assertEqual(status_code, 404)
        self.assertEqual(response, 'Not Found')


