import requests
import json

def test_account():

    url = "http://5.63.153.31:5051/v1/account"

    payload = json.dumps({
      "login": "daniil1234567",
      "email": "daniil1234567@gmail.com",
      "password": "daniil123456_789"
    })
    headers = {
      'accept': '*/*',
      'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)
