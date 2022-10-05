from selenium.webdriver.common.by import By

from constants.profile_page import ProfilePageConsts
from pages.base_page import BasePage
from pages.header import Header
from pages.utils import log_decorator


class ProfilePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = ProfilePageConsts()
        self.header = Header(self.driver)

    @log_decorator
    def follow_user(self):
        """Click on button to follow the user"""
        self.click(self.constants.FOLLOW_BUTTON_XPATH)

    @log_decorator
    def verify_followings(self, current_user, usernames):
        """Verify usernames in followings"""
        tab_xpath = self.constants.FOLLOWING_TAB_XPATH.format(username=current_user)
        assert str(len(usernames)) in self.get_element_text(tab_xpath), \
            f"Actual: {self.get_element_text(tab_xpath)}"
        self.click(tab_xpath)
        users = self.driver.find_elements(by=By.XPATH, value=self.constants.FOLLOWINGS_USERS_XPATH)
        actual_usernames = [user.text for user in users]
        assert actual_usernames == usernames
