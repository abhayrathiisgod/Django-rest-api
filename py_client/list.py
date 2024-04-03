import requests
from getpass import getpass



auth_endpoint = "http://localhost:8000/api/auth/"

username = input("enter your username\n")
password = getpass("enter your password \n")
auth_response = requests.get(auth_endpoint, json={"username": username, "password" : password}) 

print(auth_response.json())

if auth_response.status_code == 200:
    token = auth_response.json()['token']
    headers = {
        "authorization" : f"Token {token}"
    }
    endpoint = "http://localhost:8000/api/products/"
    get_response = requests.get(endpoint,headers=headers) 

    print(get_response.json())