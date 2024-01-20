import os
import random
from datetime import datetime


class Transversal:
    CO_COUNTRY = "CO"

    BROWSER = os.environ.get('BROWSER')
    NAME_REPORT = os.environ.get('NAME_REPORT')

    ENV = os.environ.get('ENV')
    TAG_NAME = os.environ.get('TAG_NAME')


class TestCategory:
    SUCCESS = "success"
    FAIL = "fail"
    IGNORE = "ignore"
    ERROR = "error"
    SKIP = "skip"
    CANCEL = "cancel"
    ALL = [SUCCESS, FAIL, IGNORE, ERROR, SKIP, CANCEL]
    ALL_UN_SUCCESSFUL = [FAIL, IGNORE, ERROR]


class SuiteCategory:
    SUCCESS = "success"
    FAIL = "fail"
    SKIP = "skip"
    CANCEL = "cancel"
    IGNORE = "ignore"
    ALL = [SUCCESS, FAIL, SKIP, CANCEL, IGNORE]
    ALL_UN_SUCCESSFUL = [FAIL, IGNORE]
    ERROR = "error"


class DecoratorType:
    TEST_SUITE = "testSuite"
    BEFORE_CLASS = "beforeClass"
    BEFORE_TEST = "beforeTest"
    AFTER_TEST = "afterTest"
    AFTER_CLASS = "afterClass"
    TEST_CASE = "testCase"
    GROUP_RULES = "groupRules"
    BEFORE_GROUP = "beforeGroup"
    AFTER_GROUP = "afterGroup"


class Event:
    ON_SUCCESS = 1
    ON_FAILURE = 2
    ON_ERROR = 3
    ON_SKIP = 4
    ON_IGNORE = 5
    ON_CANCEL = 6
    ON_CLASS_SKIP = 7
    ON_CLASS_CANCEL = 8
    ON_BEFORE_CLASS_ERROR = 9
    ON_BEFORE_CLASS_FAIL = 10
    ON_AFTER_CLASS_ERROR = 11
    ON_AFTER_CLASS_FAIL = 12
    ON_CLASS_IN_PROGRESS = 13
    ON_CLASS_COMPLETE = 14
    ON_CLASS_IGNORE = 15
    ON_BEFORE_GROUP_FAIL = 16
    ON_BEFORE_GROUP_ERROR = 17
    ON_AFTER_GROUP_FAIL = 18
    ON_AFTER_GROUP_ERROR = 19
    ON_IN_PROGRESS = 20
    ON_COMPLETE = 21


class Links:
    PAGINA_WEB = os.environ.get('PAGINA')


class Color:
    SUCCESS = "#12d479"
    FAIL = "#fcd75f"
    ERROR = "#ff7651"
    IGNORE = "#cce4eb"
    SKIP = "#34bff5"
    CANCEL = "#f19def"

    MAPPING = {TestCategory.SUCCESS: SUCCESS,
               TestCategory.FAIL: FAIL,
               TestCategory.ERROR: ERROR,
               TestCategory.IGNORE: IGNORE,
               TestCategory.SKIP: SKIP,
               TestCategory.CANCEL: CANCEL}


class TestDataBooker:
    base_url = os.environ.get('BASE_URL_BOOKER')
    HEADER = {"Content-Type": "application/json"}
    data_input = "src/json/booker/MockBooker.json"
    HEADER_UPDATEBOOKING = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Cookie": f"token="
    }
    HEADER_DELETEBOOKING = {
        "Content-Type": "application/json",
        "Cookie": f"token="
    }

    @staticmethod
    def url_CreateToken():
        return TestDataBooker.base_url + f"auth"

    @staticmethod
    def url_getBookingIds():
        return TestDataBooker.base_url + f"booking"

    @staticmethod
    def url_getHealthCheck():
        return TestDataBooker.base_url + f"ping"
