"""Sample HTTP commands"""
import random
from time import sleep

import requests

URL = "https://petstore.swagger.io/v2"

print("====================POST /user=========================")
# POST (add) user
user = {
    "id": random.randint(10000000, 99999999),
    "username": f"Lector{random.randint(10000000, 99999999)}",
    "firstName": "Denys",
    "lastName": "Kon",
    "email": "d13@dmail.com",
    "password": "133715678",
    "phone": "+374590057379",
    "userStatus": 0,
}
response = requests.request(method="POST", url=f"{URL}/user", json=user)
assert response.status_code == 200
print(response.text)
print("=" * 50)

print("=====================GET /user====================")
# GET (read) user
response = requests.request(method="GET", url=f"{URL}/user/{user['username']}")
assert response.status_code == 200
assert response.json()["userStatus"] == 1
print("=" * 50)

print("=====================PUT /user====================")
# PUT (edit) user
updated_user = {
    "id": user["id"],
    "firstName": "NewName",
    "phone": "+888888888888",
}
response = requests.request(
    method="PUT", url=f"{URL}/user/{user['username']}", json=updated_user
)
print(response.status_code)
print(response.text)
print(response.reason)
print("=" * 50)
sleep(3)

print("=====================GET /user====================")
# GET (read) user
response = requests.request(method="GET", url=f"{URL}/user/{user['username']}")
print(response.status_code)
print(response.text)
print("=" * 50)
