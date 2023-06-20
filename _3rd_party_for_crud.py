import requests
import io
import json

URL = "http://127.0.0.1:8000/crud/teacher_crud_api/"



def get_data(id = None):
    data = {}

    if id is not None:
        data = {
            'id': id,
        }

    json_data = json.dumps(data)
    res_ponce = requests.get( url = URL, data = json_data )
    data = res_ponce.json()
    print(data)

# Call get_data to Retrube data from api
# get_data(3)


def post_data():
    data = {
        'name'      : 'xyz',
        'age'       : 30,
        'salary'    : 1000000,
        'experience': True,
    }
    json_data = json.dumps(data)
    res_ponce = requests.post(url = URL, data = json_data)
    data = res_ponce.json()
    print(data)

# Call post_data to Insurt data into api
# post_data()


def update_data():
    data = {
        'id'  : 7,
        'name': 'Korim',
    }

    json_data = json.dumps(data)
    res_ponce = requests.put(url = URL, data = json_data)
    data = res_ponce.json()
    print(data)

# Call update_data to Update data from api
# update_data()



def delete_data():
    data = {
        'id': 7,
    }

    json_data = json.dumps(data)
    res_ponce = requests.delete(url = URL, data = json_data)
    data = res_ponce.json()
    print(data)

# Call delete_data to Delete data from api
# delete_data()