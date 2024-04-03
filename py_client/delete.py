import requests

id = input("enter the product id")

try:
    prod_id = int(id)
except:
    prod_id = None
    print(f'{prod_id} is not valid ')

if prod_id:
    endpoint = f"http://localhost:8000/api/products/{prod_id}/delete/"
    get_response = requests.delete(endpoint)
    print(get_response.status_code,get_response.status_code == 204)