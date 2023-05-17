from django.shortcuts import render
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

# Create your views here.
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