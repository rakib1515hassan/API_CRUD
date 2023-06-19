import requests

URL = "http://127.0.0.1:8000/Display_all_data_f"

r = requests.get(url=URL)
data = r.json()

print(data)