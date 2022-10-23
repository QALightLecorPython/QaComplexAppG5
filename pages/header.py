from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions

from constants.header import HeaderConsts
from pages.base_page import BasePage
from pages.chat import Chat
from pages.utils import log_decorator


class Header(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.constants = HeaderConsts()

    @log_decorator
    def navigate_to_create_post_page(self):
        """Click on create post button"""
        self.click(self.constants.CREATE_POST_BUTTON_XPATH)
        from pages.create_post_page import CreatePostPage

        return CreatePostPage(self.driver)

    @log_decorator
    def open_chat(self):
        """Open chat"""
        self.click(self.constants.OPEN_CHAT_XPATH)
        return Chat(self.driver)

    @log_decorator
    def navigate_to_post_via_search(self, title):
        """Navigate to post using search (by title)"""
        self.click(self.constants.SEARCH_BUTTON_XPATH)
        self.fill_field(
            xpath=self.constants.SEARCH_INPUT_FIELD_XPATH, value=title + Keys.ENTER
        )

        results = self.waiter.until(
            method=expected_conditions.visibility_of_all_elements_located(
                (By.XPATH, self.constants.SEARCH_RESULTS_XPATH)
            ),
            message=f"XPATH (elements): '{self.constants.SEARCH_RESULTS_XPATH}' is not clickable or cannot be found",
        )
        for result in results:
            if result.text == title:
                result.click()
        from pages.create_post_page import CreatePostPage

        return CreatePostPage(self.driver)

    @log_decorator
    def sign_out(self):
        """Sign Out from user account"""
        self.click(self.constants.SIGN_OUT_BUTTON_XPATH)
        from pages.start_page import StartPage

        return StartPage(self.driver)

    @log_decorator
    def navigate_to_my_profile(self):
        """Navigate to My Profile"""
        self.click(self.constants.MY_PROFILE_BUTTON_XPATH)
        from pages.profile_page import ProfilePage

        return ProfilePage(self.driver)
