import datetime
import logging
import random
import string
from time import sleep

from constants.create_post_page import CreatePostPageConsts


def random_num():
    """Generate random number"""
    return str(random.randint(111111, 999999))


def random_str(length=5):
    """Generate random string"""
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))


def wait_until_ok(timeout=5, period=0.5):
    """Reties until OK"""

    log = logging.getLogger("[WaitUntilOk]")

    def decorator(original_function):
        def wrapper(*args, **kwargs):
            end_time = datetime.datetime.now() + datetime.timedelta(seconds=timeout)
            while True:
                try:
                    return original_function(*args, **kwargs)
                except Exception as err:
                    if datetime.datetime.now() > end_time:
                        log.error(f"Catch: {err}")
                        raise err
                    sleep(period)

        return wrapper

    return decorator


def log_decorator(original_function):
    """Logging actions using docstings"""

    log = logging.getLogger("[LogDecorator]")

    def wrapper(*args, **kwargs):
        result = original_function(*args, **kwargs)
        log.info(f"{original_function.__doc__}")
        return result

    return wrapper


class User:

    def __init__(self, username="", email="", password=""):
        self.username = username
        self.email = email
        self.password = password

    def fill_data(self, username="", email="", password=""):
        """Fill user with sample data and values if provided"""
        user = random_str()
        self.username = f"{user}{random_num()}" if not username else username
        self.email = f"{user}{random_num()}@mail.com" if not email else email
        self.password = f"{random_str(6)}{random_num()}" if not password else password


class Post:

    def __init__(self, title="", body="", unique=False, private=CreatePostPageConsts.OPTION_ALL_USERS):
        self.title = title
        self.body = body
        self.unique = unique
        self.private = private

    def fill_default(self):
        """Fill fields using andom data"""
        self.title = random_str(15)
        self.body = random_str(200)
