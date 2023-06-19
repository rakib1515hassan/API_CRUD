from django.http import JsonResponse
from app.serializers import StudentSerializer
from app.models import Student
from rest_framework.renderers import JSONOpenAPIRenderer, JSONRenderer
import io
from rest_framework.parsers import JSONParser


# request.POST  # Only handles form data.  Only works for 'POST' method.
# request.data  # Handles arbitrary data.  Works for 'POST', 'PUT' and 'PATCH' methods.


# NOTE---------------------------------------( Serialization )---------------------------------------------
"""
    from app.serializers import StudentSerializer
    a = StudentSerializer()
    print(repr(a))

"""


# NOTE dumps Method-----------------------------------
# Python data -> JSON data তে convart করে 

"""
    import json
    python_data = {'name': 'Rakib', 'age': 27}
    json_data = json.dumps(python_data)
    print(json_data)
    result-> {
                "name": "Rakib",
                "roll": 27,
             }

"""

# NOTE load Method------------------------------------
# JSON data -> Python Data(parsed data) তে convart করে 

"""
    json_data = {"name": "Rakib", "roll": 27}
    python_data = json.loads(json_data)
    print(python_data)
    result-> {'name': 'Rakib', 'age': 27}

"""

# NOTE START-----------------------( Serialization )--------------------------------------------------------------------
# The process of converting complex data such as querysets and model instance to native Python datatype are called.....
# as Serialization in DRF.

# Create model instance std
std = Student.objects.get(id = 1)
# Converting model instance std to Python Dictanary/Serializing Object
serializ = StudentSerializer(std)

# IF QUERRY SET:
# Create model instance std
std = Student.objects.all()
# Converting model instance std to Python Dictanary/Serializing Object
serializ = StudentSerializer(std, many = True)

# To see Serialization data
print(serializ.dat)


# NOTE START-----------------------( JSONRenderer )--------------------------------------------------------------------
# This is used to render Serialized data into JSON which is understandable by Front End.

# Render the data into Json 
json_data = JSONRenderer().render(serializ.dat)



# NOTE START-----------------------( JsonResponse )--------------------------------------------------------------------

"""

An HttpResponce subclass that helps to create a JSON-encoded response. It inherits most behevior from it's
superclass with a couple differences.

1) It's default Content-Type header is set to application/json.

2) The first parameter, data, should be a dictionary instance. If the safe parameter is set to False it 
   can be any JSON-serializable object.

3) The encoder, which defaults to django.core.serializers.json.DjangoJSONEncoder, will be used to serialize the data.

4) The safe boolean parameter defaults to True. If it's set to False, any object can be passed for serialization
   (otherwise only dictionary instance are allowed) If safe is True and non-dictionary object is passed as the first argument,
   a TypeError will be raised. 

5) The json_dumps_params parameter is a dictionary of keyword arguments to pass to the json.dumps() call used to generate the response.

Example:-

        JsonResponse(data, encoder = DjangoJSONEncoder, safe = True, json_dumps_params = None, **kwargs)

"""


# NOTE---------------------------------------( De-Serialization )---------------------------------------------

# BytesIO() make stream data
stream = io.BytesIO(json_data)

# JSONParser() make parsed_data
parsed_data = JSONParser().parse(stream)


# Creating Serializer Object 
serializer_obj = StudentSerializer(data = parsed_data)