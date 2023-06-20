import requests
import json
URL = "http://127.0.0.1:8000/note/3rd-parti-api/"


raw_data = {
    'name':'Merina',
    'student_class':'x',
    'gender':'Female',
    'roll':420,
    'email':'merina@gmail.com',
    'waiver':'False',
    'description':"Merina is't a good student.",
    'date_of_birth':'1999-02-15',
}

json_data = json.dumps(raw_data)
res_ponce = requests.post(url = URL, data = json_data)

data = res_ponce.json()
print(data)