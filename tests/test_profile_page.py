import allure
import pytest
from allure_commons.types import Severity

from constants.base import CHROME, FIREFOX
from pages.utils import Post, User


@pytest.mark.parametrize("browser", [CHROME, FIREFOX])
class TestProfilePage:
    @pytest.fixture()
    def hello_page(self, start_page, random_user):
        """Sign Up as the user and return the page"""
        return start_page.sign_up_and_verify(random_user)

    @pytest.fixture()
    def user_with_post(self, start_page):
        """Sign up as a user and create post, sign out"""
        user = User()
        user.fill_data()
        # Sign up
        hello_page = start_page.sign_up_and_verify(user)

        # Navigate to create Post Page
        create_post_page = hello_page.header.navigate_to_create_post_page()

        # Create Post
        post = Post()
        post.fill_default()
        create_post_page.create_post(post)
        user.posts.append(post)

        # Sign Out
        create_post_page.header.sign_out()

        return user

    @allure.epic("Profile Page")
    @allure.feature("Following")
    @allure.story("Test followings tab")
    @allure.severity(Severity.NORMAL)
    def test_followings(self, user_with_post, hello_page, random_user):
        """
        - Pre-conditions:
            - Sign up as a user (user1)
            - Create a post
            - Sign Out
            - Sign Up as the other user (user2)
        - Steps:
            - Search  for post by user1
            - Navigate to post
            - Navigate to the user profile
            - Follow the user
            - Navigate to user2 profile
            - Verify following tab
        """
        post = user_with_post.posts[0]

        # Search for post by user1
        post_page = hello_page.header.navigate_to_post_via_search(post.title)

        # Navigate to the user profile
        profile_page = post_page.navigate_to_profile(user_with_post.username.lower())

        # Follow the user
        profile_page.follow_user()

        # Navigate to user2 profile
        profile_page.header.navigate_to_my_profile()

        # Verify following tab
        profile_page.verify_followings(
            current_user=random_user.username.lower(),
            usernames=[user_with_post.username.lower()],
        )
