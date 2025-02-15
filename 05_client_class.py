import requests
import json
import pytest
from faker import Faker
from client import Client

@pytest.fixture
def client():
    return Client()

@pytest.fixture
def generate_user():
    fake = Faker("ru_RU")
    return {
        "login": fake.user_name(),
        "email": fake.email(),
        "password": fake.password()
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
def test_post_v1_account(data, client):
    print(data)
    response = client.register_user(data)
    print(response.text)
