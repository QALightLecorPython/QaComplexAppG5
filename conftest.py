import datetime
import os

import pytest as pytest

from constants.base import BASE_URL, DRIVER_PATH
from pages.start_page import StartPage
from pages.utils import User, create_driver


def pytest_sessionstart(session):
    os.environ["PATH"] = (os.environ["PATH"] + f":{os.path.abspath(DRIVER_PATH)}")


@pytest.fixture(scope="function")
def start_page(browser):
    # Pre-conditions
    driver = create_driver(browser)
    driver.get(BASE_URL)
    # Steps
    yield StartPage(driver)
    # Post-conditions
    driver.close()


@pytest.fixture()
def random_user():
    user = User()
    user.fill_data()
    return user


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Preserve screenshot on failure"""
    outcome = yield
    result = outcome.get_result()

    if result.failed:
        driver = [item.funcargs[arg] for arg in item.funcargs if arg.endswith("_page")][0].driver  # hello_page.driver
        file_name = f"{item.name}_{datetime.datetime.now().strftime('%H-%M-%S')}.png"
        file_path = "/Users/deniskondratuk/PycharmProjects/G5/QaComplexAppG5/screenshots"
        driver.save_screenshot(os.path.join(file_path, file_name))
