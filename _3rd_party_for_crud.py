import requests
import io
import json

# URL = "http://127.0.0.1:8000/crud-1/teacher_crud_api/"
# URL = "http://127.0.0.1:8000/crud-1/Teacher_crud_classApiView/"


URL = "http://127.0.0.1:8000/crud-2/teacher_crud_api/"



def get_data(id = None):
    data = {}

    if id is not None:
        data = {
            'id': id,
        }

    json_data = json.dumps(data)
    header = {'content-Type': 'application/json'} ## CRUD_2 app এর url Test করা জন্যে দরকার
    res_ponce = requests.get( url = URL, data = json_data, headers= header)
    data = res_ponce.json()
    print(data)

# Call get_data to Retrube data from api
# get_data(1)






def post_data():
    data = {
        'name'      : 'xyz',
        'age'       : 30,
        'salary'    : 1000000,
        'experience': True,
    }
    json_data = json.dumps(data)
    header = {'content-Type': 'application/json'} ## CRUD_2 app এর url Test করা জন্যে দরকার
    res_ponce = requests.post(url = URL, data = json_data, headers= header)
    data = res_ponce.json()
    print(data)

# Call post_data to Insurt data into api
# post_data()






def update_data():
    data = {
        'id'  : 10,
        'name': 'Korim',
    }

    json_data = json.dumps(data)
    header = {'content-Type': 'application/json'} ## CRUD_2 app এর url Test করা জন্যে দরকার
    res_ponce = requests.put(url = URL, data = json_data, headers= header)
    data = res_ponce.json()
    print(data)

# Call update_data to Update data from api
# update_data()






def delete_data():
    data = {
        'id': 10,
    }

    json_data = json.dumps(data)
    header = {'content-Type': 'application/json'} ## CRUD_2 app এর url Test করা জন্যে দরকার
    res_ponce = requests.delete(url = URL, data = json_data, headers= header)
    data = res_ponce.json()
    print(data)

# Call delete_data to Delete data from api
# delete_data()