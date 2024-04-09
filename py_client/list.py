import requests
from getpass import getpass


auth_endpoint = "http://localhost:8000/api/auth/"

username = input("enter your username\n")
password = getpass("enter your password \n")
auth_response = requests.get(
    auth_endpoint, json={"username": username, "password": password})

print(auth_response.json())

if auth_response.status_code == 200:
    token = auth_response.json()['token']
    headers = {
        "authorization": f"Token {token}"
    }
    endpoint = "http://localhost:8000/api/products/"
    get_response = requests.get(endpoint, headers=headers)

    print(get_response.json())

    #
    #           below code can be done recursively, if we want all the data
    # data = get_response.json()
    # next_url = data['next']
    # if next_url is not None:
    #     get_response = requests.get(next_url ,headers=headers)
    #     print(get_response.json())
