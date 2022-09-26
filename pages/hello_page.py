from constants.hello_page import HelloPageConsts
from pages.base_page import BasePage
from pages.header import Header


class HelloPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = HelloPageConsts()
        self.header = Header(self.driver)

    def verify_success_sign_up(self, username):
        """Verify success Sign Up using hello message"""
        username = username.lower()
        assert self.get_element_text(self.constants.HELLO_MESSAGE_XPATH) == self.constants.HELLO_MESSAGE_TEXT.format(username=username), \
            f"Actual message: {self.get_element_text(self.constants.HELLO_MESSAGE_XPATH)}"

        assert self.get_element_text(self.constants.HELLO_MESSAGE_USERNAME_XPATH) == username, \
            f"Actual message: {self.get_element_text(self.constants.HELLO_MESSAGE_USERNAME_XPATH)}"
