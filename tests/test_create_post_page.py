import logging

import pytest

from constants.create_post_page import CreatePostPageConsts
from pages.utils import Post, random_str


class TestCreatePostPage:
    log = logging.getLogger("[CreatePostPage]")

    @pytest.fixture()
    def hello_page(self, start_page, random_user):
        """Sign Up as the user and return the page"""
        return start_page.sign_up_and_verify(random_user)

    def test_create_post_page(self, hello_page):
        """
        - Pre-conditions:
            - Sign Up/Sign In as an user
        - Steps:
            - Navigate to create Post Page
            - Create Post
            - Verify the result
        """
        # Navigate to create Post Page
        create_post_page = hello_page.header.navigate_to_create_post_page()

        # Create Post
        post = Post()
        post.fill_default()
        create_post_page.create_post(post)

        # Verify the result
        create_post_page.verify_successfully_created()

    def test_create_full_post(self, hello_page):
        """
        - Pre-conditions:
            - Sign Up/Sign In as an user
        - Steps:
            - Fill title, body, select check box, choose visibility adn click on crete button
            - Verify that data match to expected
        """
        # Navigate to create Post Page
        create_post_page = hello_page.header.navigate_to_create_post_page()

        # Create Post
        post = Post(title=random_str(15), body=random_str(20), unique=True, private=CreatePostPageConsts.OPTION_GROUP_MESSAGE)
        create_post_page.create_post(post)

        # Verify the result
        create_post_page.verify_full_post_data(post)
