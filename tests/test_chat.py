import logging

import allure
import pytest
from allure_commons.types import Severity

from constants.base import CHROME, FIREFOX
from pages.utils import random_str


@pytest.mark.parametrize("browser", [CHROME, FIREFOX])
class TestChat:
    log = logging.getLogger("[CreatePostPage]")

    @pytest.fixture()
    def hello_page(self, start_page, random_user):
        """Sign Up as the user and return the page"""
        return start_page.sign_up_and_verify(random_user)

    @allure.epic("Chat")
    @allure.feature("Send messages")
    @allure.story("Test chat messages sending")
    @allure.severity(Severity.CRITICAL)
    def test_chat(self, hello_page):
        """
        - Pre-conditions:
            - Sign Up/Sign In as an user
        - Steps:
            - Open chat
            - Send message
            - Verify message
            - Send one more message
            - Verify messages
        """
        chat = hello_page.header.open_chat()

        # Send message
        message_1 = random_str(10)
        chat.send_message(message_1)

        # Verify message
        chat.verify_messages([message_1])

        # Send one more message
        message_2 = random_str(30)
        chat.send_message(message_2)

        # Verify message
        chat.verify_messages([message_1, message_2])
