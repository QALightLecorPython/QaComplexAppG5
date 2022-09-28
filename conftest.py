import pytest as pytest
from selenium import webdriver

from constants.base import DRIVER_PATH, BASE_URL
from pages.start_page import StartPage
from pages.utils import User


@pytest.fixture(scope="function")
def start_page():
    # Pre-conditions
    driver = webdriver.Chrome(DRIVER_PATH)
    driver.get(BASE_URL)
    driver.implicitly_wait(1)
    # Steps
    yield StartPage(driver)
    # Post-conditions
    driver.close()


@pytest.fixture()
def random_user():
    user = User()
    user.fill_data()
    return user
