import requests
import json
import pytest
from faker import Faker

@pytest.fixture
def generate_user():
    fake = Faker("ru_RU")
    return {
        "login": fake.user_name(),
        "email": fake.email(),
        "password": fake.password()
    }

@pytest.fixture
def set_url():
    return "http://5.63.153.31:5051/v1/account"

@pytest.fixture
def headers():
    return {
        'accept': '*/*',
        'Content-Type': 'application/json'
    }

data = [
    # short login
    {
        "login": "l",
        "email": "email_12345@mail.ru",
        "password": "12345678"
    },
    # non-valid email
    {
        "login": "login_125236437347",
        "email": "e",
        "password": "12345678"
    },
    # short password
    {
        "login": "login_125236437348",
        "email": "email_12345@mail.ru",
        "password": "p"
    }
]

@pytest.mark.parametrize('data', data)
def test_post_v1_account(set_url, headers, data):
    print(data)
    response = requests.request("POST", set_url, headers=headers, json=data)
    print(response.text)
