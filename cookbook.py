import requests

url = "http://localhost:8000"

payload = ""
# headers = {
#     'Content-Type': "application/json",
#     'Authorization': "Basic a2F1c2hpay5zYXJrYXJAbmV3cGFnZS5pb286a2F1c2hpa0AxMjM=",
#     'cache-control': "no-cache",
#     'Postman-Token': "13aba541-5cb2-4613-b6d5-1390f7c65771"
#     }

response = requests.request("POST", url)

# print(response.text)