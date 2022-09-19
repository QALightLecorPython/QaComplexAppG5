import logging

import pytest
from selenium import webdriver

from constants.base import DRIVER_PATH, BASE_URL
from pages.start_page import StartPage
from pages.utils import random_str, random_num


class TestStartPage:
    log = logging.getLogger("[StartPage]")

    @pytest.fixture(scope="function")
    def start_page(self):
        # Pre-conditions
        driver = webdriver.Chrome(DRIVER_PATH)
        driver.get(BASE_URL)
        # Steps
        yield StartPage(driver)
        # Post-conditions
        driver.close()

    @pytest.fixture(scope="function")
    def start_page(self):
        # Pre-conditions
        driver = webdriver.Chrome(DRIVER_PATH)
        driver.get(BASE_URL)
        # Steps

    @pytest.fixture(scope="function")
    def start_page(self):
        # Pre-conditions
        driver = webdriver.Chrome(DRIVER_PATH)
        driver.get(BASE_URL)
        # Steps
        return StartPage(driver)

    @pytest.fixture(scope="function")
    def start_page(self):
        # Steps
        yield
        # Post-conditions
        # Some actions

    def test_incorrect_login(self, start_page):
        """
        - Pre-conditions:
            - Create driver
            - Open page
        - Steps:
            - Fill login
            - Fill password
            - Click button
            - Verify error
        - Post-conditions:
            - Close driver
        """
        # Login as a user
        start_page.sign_in("User11", "Psw11")
        self.log.info("Logged in as non-existing user")

        # Verify error
        start_page.verify_sign_in_error()
        self.log.info("Error was verified")

    def test_empty_login(self, start_page):
        """
        - Create driver
        - Open page
        - Clear login
        - Clear password
        - Click button
        - Verify error
        """
        # Login as a user
        start_page.sign_in("", "")
        self.log.info("Logged in as non-existing user")

        # Verify error
        start_page.verify_sign_in_error()
        self.log.info("Error was verified")

    def test_register(self, start_page):
        """
        - Pre-conditions:
            - Open start page
        - Steps:
            - Fill email, login and password fields
            - Click on Sign Up button
            - Verify registration is successful
        """
        # Prepare data
        user = random_str()
        username_value = f"{user}{random_num()}"
        email_value = f"{user}{random_num()}@mail.com"
        password_value = f"{random_str(6)}{random_num()}"

        # Sign Up as a user
        start_page.sign_up(username_value, email_value, password_value)
        self.log.info("Signed Up as user %s", username_value)

        # Verify success message
        start_page.verify_success_sign_up(username_value)
        self.log.info("Hello message was verified")
