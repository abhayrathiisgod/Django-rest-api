import requests

endpoint = "http://localhost:8000/api/products/1"

get_response = requests.post(endpoint, json={"title": "abc123", "content": "Hello world" , "price":"1234"}) 

print(get_response.json())