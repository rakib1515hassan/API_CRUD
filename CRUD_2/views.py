from django.shortcuts import render, redirect
from app.serializers import StudentSerializer
from ApiNote.serializer import TeacherSerializer
from app.models import Student
from ApiNote.models import Teacher

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
import io

from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework import status


# Create your views here.
# URL = ( http://127.0.0.1:8000/crud-2/teacher_crud_api/ )
@api_view( ['GET', 'POST', 'PUT','PATCH', 'DELETE'] )
def teacher_crud_api(request, pk = None):

    if request.method == "GET":
        # id = request.data.get('id') ## For _3rd_party_for_crud.py এর জন্যে এটি দরকার
        id = pk

        if id is not None:
            teacher = Teacher.objects.get(id = id)
            serializer = TeacherSerializer(teacher)
            return Response(serializer.data)

        teacher = Teacher.objects.all()
        serializer = TeacherSerializer(teacher, many = True)
        return Response(serializer.data)
    



    if request.method == "POST":
        serializer = TeacherSerializer( data = request.data )
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data is successfully save in Database.'}
            return Response( {'res':res} )
        
        return Response( serializer.errors )
    


    
    if request.method == "PUT":
        # id = request.data.get('id') ## For _3rd_party_for_crud.py এর জন্যে এটি দরকার
        id = pk

        teacher =Teacher.objects.get(id = id)

        # serializer = TeacherSerializer( teacher,  data = request.data, partial = True ) ## For _3rd_party_for_crud.py এর জন্যে
        serializer = TeacherSerializer( teacher,  data = request.data )
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data is successfully Update in Database.'}
            return Response( {'res':res} )
        
        return Response( serializer.errors )
    



    if request.method == "PATCH":
        id = pk

        teacher =Teacher.objects.get(id = id)

        ## নির্দিষ্ট কিছু Field কে Update করাই হল Partial Update
        serializer = TeacherSerializer( teacher,  data = request.data, partial = True )
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Partial Update in Database.'}
            return Response( {'res':res} )
        
        return Response( serializer.errors )
    



    if request.method == "DELETE":
        # id = request.data.get('id') ## For _3rd_party_for_crud.py এর জন্যে এটি দরকার
        id = pk

        teacher =Teacher.objects.get(id = id)
        teacher.delete()
        res = {'msg': 'Data Successfully Deleted.'}
        return Response( {'res':res} )
    








