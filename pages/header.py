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
