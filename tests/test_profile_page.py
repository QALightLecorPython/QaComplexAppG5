import pytest as pytest

from pages.utils import Post, User


class TestProfilePage:

    @pytest.fixture()
    def hello_page(self, start_page, random_user):
        """Sign Up as the user and return the page"""
        return start_page.sign_up_and_verify(random_user)

    def test_followings(self, hello_page, random_user):
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
        # Navigate to create Post Page
        create_post_page = hello_page.header.navigate_to_create_post_page()

        # Create Post
        post = Post()
        post.fill_default()
        create_post_page.create_post(post)

        # Sign Out
        start_page = create_post_page.header.sign_out()

        # Sign Up as the other user (user2)
        user2 = User()
        user2.fill_data()
        hello_page = start_page.sign_up_and_verify(user2)

        # Search  for post by user1
        post_page = hello_page.header.navigate_to_post_via_search(post.title)

        # Navigate to the user profile
        profile_page = post_page.navigate_to_profile(random_user.username.lower())

        # Follow the user
        profile_page.follow_user()

        # Navigate to user2 profile
        profile_page.header.navigate_to_my_profile()

        # Verify following tab
        profile_page.verify_followings(current_user=user2.username.lower(), usernames=[random_user.username.lower()])
