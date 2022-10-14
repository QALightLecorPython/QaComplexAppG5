import logging

import allure
import pytest
from allure_commons.types import Severity

from constants.base import CHROME, FIREFOX
from pages.utils import User


@pytest.mark.parametrize("browser", [CHROME, FIREFOX])
class TestStartPage:
    log = logging.getLogger("[StartPage]")

    @allure.epic("Start Page")
    @allure.feature("Sign In")
    @allure.story("Test Incorrect Sign In")
    @allure.severity(Severity.MINOR)
    def test_incorrect_login(self, start_page, random_user):
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
        start_page.sign_in(random_user)

        # Verify error
        start_page.verify_sign_in_error()

    @allure.epic("Start Page")
    @allure.feature("Sign In")
    @allure.story("Test Incorrect Sign In")
    @allure.severity(Severity.TRIVIAL)
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
        start_page.sign_in(User())

        # Verify error
        start_page.verify_sign_in_error()

    @allure.epic("Start Page")
    @allure.feature("Sign Up")
    @allure.story("Test Sign Up")
    @allure.severity(Severity.CRITICAL)
    def test_register(self, start_page, random_user):
        """
        - Pre-conditions:
            - Open start page
        - Steps:
            - Fill email, login and password fields
            - Click on Sign Up button
            - Verify registration is successful
        """
        # Sign Up as a user
        hello_page = start_page.sign_up_and_verify(random_user)

        # Verify success message
        hello_page.verify_success_sign_up(random_user.username)
