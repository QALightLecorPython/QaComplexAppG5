from constants.start_page import StartPageConstants
from pages.base_page import BasePage
from pages.utils import wait_until_ok, log_decorator


class StartPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = StartPageConstants()

    @log_decorator
    def sign_in(self, user):
        """Sign in as the user"""
        # Fill login
        self.fill_field(xpath=self.constants.SIGN_IN_USERNAME_FIELD_XPATH, value=user.username)
        self.fill_field(xpath=self.constants.SIGN_IN_PASSWORD_FIELD_XPATH, value=user.password)
        # Click button
        self.click(xpath=self.constants.SIGN_IN_BUTTON_XPATH)

    @log_decorator
    def verify_sign_in_error(self):
        """Verify invalid Sign In error"""
        assert self.get_element_text(self.constants.SIGN_IN_LOGIN_ERROR_XPATH) == self.constants.SIGN_IN_LOGIN_ERROR_TEXT, \
            f"Actual message: {self.get_element_text(self.constants.SIGN_IN_LOGIN_ERROR_XPATH)}"

    @log_decorator
    def sign_up_and_verify(self, user):
        """Sign up as the user and verify that you're inside"""
        # Fill username
        self.fill_field(xpath=self.constants.SIGN_UP_USERNAME_FIELD_XPATH, value=user.username)
        self.fill_field(xpath=self.constants.SIGN_UP_EMAIL_FIELD_XPATH, value=user.email)
        self.fill_field(xpath=self.constants.SIGN_UP_PASSWORD_FIELD_XPATH, value=user.password)
        # Click button
        self.click_sign_up_and_verify()
        # Return new page
        from pages.hello_page import HelloPage
        return HelloPage(self.driver)

    @log_decorator
    def sign_up(self, user):
        """Sign up as the user and verify that you're inside"""
        # Fill username
        self.fill_field(xpath=self.constants.SIGN_UP_USERNAME_FIELD_XPATH, value=user.username)
        self.fill_field(xpath=self.constants.SIGN_UP_EMAIL_FIELD_XPATH, value=user.email)
        self.fill_field(xpath=self.constants.SIGN_UP_PASSWORD_FIELD_XPATH, value=user.password)
        # Click button
        self.click(xpath=self.constants.SIGN_UP_BUTTON_XPATH)

    @wait_until_ok(period=0.5)
    def click_sign_up_and_verify(self):
        """Click Sign Up button and verify"""
        # Click button
        self.click(xpath=self.constants.SIGN_UP_BUTTON_XPATH)
        assert not self.is_exists(xpath=self.constants.SIGN_UP_BUTTON_XPATH)
