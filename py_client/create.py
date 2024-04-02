import requests

endpoint = "http://localhost:8000/api/products/"

data = {
    "title" : "THIS FIELD IS DONE"
}

get_response = requests.post(endpoint,data) 

print(get_response.json())