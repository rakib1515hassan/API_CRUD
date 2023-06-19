from django.shortcuts import render
from django.http import HttpResponse
from app.models import Student
from app.serializers import StudentSerializer

# Function View
from rest_framework.decorators import api_view
# Class View
from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONOpenAPIRenderer, JSONRenderer

# Exception
from django.core.exceptions import ObjectDoesNotExist

# NOTE Start ------------------------------------------------------

# Create -> POST
# Read   -> GET
# Update -> PUT, PATCH
# Delete -> DELETE

# request.POST  # Only handles form data.  Only works for 'POST' method.
# request.data  # Handles arbitrary data.  Works for 'POST', 'PUT' and 'PATCH' methods.

# NOTE End --------------------------------------------------------


# Create your views here.
def home(request):
    return render(request, 'index.html')


# ---------------------------( 1 )--------------------------------------------------
def Display_a_data_f(request, pk):
    obj = Student.objects.get(id=pk) #Complex data or Querry 
    serializer = StudentSerializer(obj) # Python data type

    #json_data = JSONRenderer().render(serializer.data) #covart in to json data
    # return HttpResponse(json_data, content_type='application/json')
    return JsonResponse(serializer.data) # উপরের ২ লাইন এর পরিবর্তে আমরা JsonResponse ব্যবহার করতে পারি
    
    # try:
    #     obj = Student.objects.get(id=pk) #Complex data or Querry 
    #     serializer = StudentSerializer(obj) # Python data type

    #     # json_data = JSONRenderer().render(serializer.data) #covart in to json data
    #     # return HttpResponse(json_data, content_type='application/json')
    #     return JsonResponse(serializer.data) # উপরের ২ লাইন এর পরিবর্তে আমরা JsonResponse ব্যবহার করতে পারি
    
    # except Student.DoesNotExist:
    #     return Response(StudentSerializer.errors, status=status.HTTP_404_NOT_FOUND)

    

# class DisplayDataAPIView(APIView):
#     def get(self, request, pk):
#         try:
#             obj = Student.objects.get(id=pk)  # Complex data or Query
#         except Student.DoesNotExist:
#             return Response("Student not found", status=status.HTTP_404_NOT_FOUND)

#         serializer = StudentSerializer(obj)  # Python data type
#         json_data = serializer.data  # Convert to JSON data

#         return Response(json_data, content_type='application/json')


# ---------------------------( 2 )--------------------------------------------------
def Display_all_data_f(request):
    obj = Student.objects.all() #Complex data or Querry 
    serializer = StudentSerializer(obj, many = True) # Python data type for multiple Querry

    # json_data = JSONRenderer().render(serializer.data) #covart in to json data
    # return HttpResponse(json_data, content_type='application/json')
    return JsonResponse(serializer.data, safe=False) # উপরের ২ লাইন এর পরিবর্তে আমরা JsonResponse 
                                         # ব্যবহার করতে পারি তবে যেহেতু এখানে dictinary
                                         # data type হতে হবে তাই by deffult safe=True
                                         # কে safe=False করে দিতে হবে।



# ---------------------------( 3 )--------------------------------------------------










## ---------------------------- Display With GET Method --------------------------------------
@api_view(['GET'])
def display_function_view(request):
    if request.method == 'GET':
        obj = Student.objects.all()
        serializer = StudentSerializer(obj, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(StudentSerializer.errors, status=status.HTTP_404_NOT_FOUND)



class display_class_view(APIView):
    def get(self, request):
        obj = Student.objects.all()
        serializer = StudentSerializer(obj, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

## ---------------------------- Display With POST Method --------------------------------------

@api_view(['POST'])
def display_function_view_POST(request):
    if request.method == 'POST':
        serialize = StudentSerializer(data= request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data, status=status.HTTP_200_OK)
        return Response(StudentSerializer.errors, status=status.HTTP_404_NOT_FOUND)


## --------------------------------------------------------------------------------------------

@csrf_exempt
def student_detail(request, pk):
    try:
        a = Student.objects.get(pk=pk)
    except a.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = StudentSerializer(a)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = StudentSerializer(a, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        a.delete()
        return HttpResponse(status=204)
    

@api_view(['GET', 'POST'])
def snippet_list(request):

    if request.method == 'GET':
        snippets = Student.objects.all()
        serializer = StudentSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)