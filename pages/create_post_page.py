from constants.create_post_page import CreatePostPageConsts
from pages.base_page import BasePage
from pages.utils import log_decorator, Post


class CreatePostPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.constants = CreatePostPageConsts()
        from pages.header import Header

        self.header = Header(self.driver)

    @log_decorator
    def create_post(self, post):
        """Create post using provided values"""
        self.fill_field(xpath=self.constants.TITLE_FIELD_XPATH, value=post.title)
        self.fill_field(xpath=self.constants.BODY_FIELD_XPATH, value=post.body)
        # Click on checkbox if required
        if post.unique:
            self.click(xpath=self.constants.UNIQUE_POST_CHECKBOX_XPATH)
        # Click on list
        self.click(xpath=self.constants.VISIBILITY_LIST_XPATH)
        # Click on option
        self.click(
            self.constants.VISIBILITY_SELECTION_XPATH.format(option=post.private)
        )
        self.click(xpath=self.constants.CREATE_POST_BUTTON_XPATH)

    @log_decorator
    def verify_successfully_created(self):
        """Verify success message"""
        assert (
                self.get_element_text(xpath=self.constants.SUCCESS_MESSAGE_XPATH)
                == self.constants.SUCCESS_MESSAGE_TEXT
        ), f"Actual: {self.get_element_text(xpath=self.constants.SUCCESS_MESSAGE_XPATH)}"

    @log_decorator
    def verify_full_post_data(self, post: Post):
        """Verify all post fields"""
        # Verify title
        assert (
                self.get_element_text(xpath=self.constants.CREATED_TITLE_XPATH)
                == post.title
        ), f"Actual: {self.get_element_text(xpath=self.constants.CREATED_TITLE_XPATH)}"
        # Verify private
        assert (
                self.get_element_text(xpath=self.constants.CREATED_VISIBILITY_VALUE_XPATH)
                == post.private
        ), f"Actual: {self.get_element_text(xpath=self.constants.CREATED_VISIBILITY_VALUE_XPATH)}"
        # Verify checkbox value
        if post.unique:
            assert "yes" in self.get_element_text(
                xpath=self.constants.IS_POST_UNIQUE_XPATH
            )
        else:
            assert "no" in self.get_element_text(
                xpath=self.constants.IS_POST_UNIQUE_XPATH
            )
        # Verify body
        assert (
                self.get_element_text(
                    xpath=self.constants.CREATED_BODY_CONTENT_XPATH.format(body=post.body)
                )
                == post.body
        )

    @log_decorator
    def navigate_to_profile(self, username):
        """Navigate to author profile"""
        self.click(self.constants.PROFILE_LINK_XPATH.format(username=username))
        from pages.profile_page import ProfilePage

        return ProfilePage(self.driver)
