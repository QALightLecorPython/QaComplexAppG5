"""Swagger codegen samples"""
import random
from typing import Tuple

# pylint: disable=import-error
from apis.swagger_client.api.user_api import UserApi
from apis.swagger_client.api_client import ApiClient
from apis.swagger_client.configuration import Configuration
from apis.swagger_client.models.user import User

from pages.utils import wait_until_ok


@wait_until_ok(15)
def wait_for_user(user_name: str = "name") -> User:
    """Retry until ok decorator"""
    return user_api.get_user_by_name(username=user_name)


if __name__ == "__main__":
    # Create API
    api_client = ApiClient(configuration=Configuration())
    user_api = UserApi(api_client=ApiClient())

    print("====================POST /user=========================")
    # Create user
    # - Prepare data using model
    username = f"Lector{random.randint(10000000, 99999999)}"
    user = User(
        id=random.randint(10000000, 99999999),
        username=username,
        first_name="John",
        last_name="Doe",
        email="jdoe@mail.com",
        password="123456",
        phone="+2345655",
    )
    # - Send request
    response: Tuple = user_api.create_user_with_http_info(user)
    # - Check the response
    print(response)
    print(response[1])
    print("=" * 50)

    print("=====================GET /user====================")
    # Get user
    response: User = wait_for_user(username)
    print(response.email)
    print("=" * 50)

    # Close connections
    del user_api
    del api_client
