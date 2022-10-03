from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from constants.chat import ChatConsts
from pages.base_page import BasePage
from pages.utils import log_decorator


class Chat(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = ChatConsts()

    @log_decorator
    def send_message(self, message):
        """Send provided message"""
        self.fill_field(xpath=self.constants.CHAT_INPUT_XPATH, value=message + Keys.ENTER)

    @log_decorator
    def verify_messages(self, expected_messages):
        """Verify messages"""
        messages = self.driver.find_elements(by=By.XPATH, value=self.constants.CHAT_MESSAGES_XPATH)
        messages_text = [message.text for message in messages]
        assert messages_text == expected_messages
