from django.shortcuts import render
from app.models import Student
from app.serializers import StudentSerializer

# Function View
from rest_framework.decorators import api_view
# Class View
from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework import status


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