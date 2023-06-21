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

from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework import status


# Create your views here.
@csrf_exempt
def teacher_crud_api(request):

    if request.method == "GET":
        jason_data = request.body
        stream = io.BytesIO(jason_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id', None)

        if id is not None:
            teacher = Teacher.objects.get(id = id)
            serializer = TeacherSerializer(teacher)
            # json_data = JSONRenderer().render(serializer.data)
            # return HttpResponse(json_data, content_type = 'application/json')
            return JsonResponse(serializer.data, safe=False) # উপরের ২ লাইন এর পরিবর্তে আমরা JsonResponse 
                                         # ব্যবহার করতে পারি তবে যেহেতু এখানে dictinary
                                         # data type হতে হবে তাই by deffult safe=True
                                         # কে safe=False করে দিতে হবে।

        teacher = Teacher.objects.all()
        serializer = TeacherSerializer(teacher, many = True)
        # json_data = JSONRenderer().render(serializer.data)
        # return HttpResponse(json_data, content_type = 'application/json')
        return JsonResponse( serializer.data, safe=False ) # উপরের ২ লাইন এর পরিবর্তে
        

    if request.method == "POST":
        jason_data = request.body
        stream = io.BytesIO(jason_data)
        python_data = JSONParser().parse(stream)

        serializer = TeacherSerializer( data = python_data )
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data is successfully save in Database.'}
            # json_data = JSONRenderer().render(res)
            # return HttpResponse(json_data, content_type = 'application/json')
            return JsonResponse( res, safe=False ) # উপরের ২ লাইন এর পরিবর্তে
        
        # json_data = JSONRenderer().render(serializer.errors)
        # return HttpResponse(json_data, content_type = 'application/json')
        return JsonResponse( serializer.errors, safe=False ) # উপরের ২ লাইন এর পরিবর্তে
    
    if request.method == "PUT":
        jason_data = request.body
        stream = io.BytesIO(jason_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        teacher =Teacher.objects.get(id = id)

        ## নির্দিষ্ট কিছু Field কে Update করাই হল Partial Update
        serializer = TeacherSerializer( teacher,  data = python_data, partial = True )
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data is successfully Update in Database.'}
            # json_data = JSONRenderer().render(res)
            # return HttpResponse(json_data, content_type = 'application/json')
            return JsonResponse( res, safe=False ) # উপরের ২ লাইন এর পরিবর্তে
        
        # json_data = JSONRenderer().render(serializer.errors)
        # return HttpResponse(json_data, content_type = 'application/json')
        return JsonResponse(serializer.errors, safe=False) # উপরের ২ লাইন এর পরিবর্তে
    

    if request.method == "DELETE":
        jason_data = request.body
        stream = io.BytesIO(jason_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        teacher =Teacher.objects.get(id = id)
        teacher.delete()

        res = {'msg': 'Data Successfully Deleted.'}
        # json_data = JSONRenderer().render(res)
        # return HttpResponse(json_data, content_type = 'application/json')
        return JsonResponse( res, safe=False ) # উপরের ২ লাইন এর পরিবর্তে
    










@method_decorator( csrf_exempt, name= 'dispatch' )
class Teacher_crud_classApiView(View):
    def get(self, request, *args, **kwargs):
        jason_data = request.body
        stream = io.BytesIO(jason_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id', None)

        if id is not None:
            teacher = Teacher.objects.get(id = id)
            serializer = TeacherSerializer(teacher)
            # json_data = JSONRenderer().render(serializer.data)
            # return HttpResponse(json_data, content_type = 'application/json')
            return JsonResponse(serializer.data, safe=False) # উপরের ২ লাইন এর পরিবর্তে আমরা JsonResponse 
                                         # ব্যবহার করতে পারি তবে যেহেতু এখানে dictinary
                                         # data type হতে হবে তাই by deffult safe=True
                                         # কে safe=False করে দিতে হবে।

        teacher = Teacher.objects.all()
        serializer = TeacherSerializer(teacher, many = True)
        # json_data = JSONRenderer().render(serializer.data)
        # return HttpResponse(json_data, content_type = 'application/json')
        return JsonResponse( serializer.data, safe=False ) # উপরের ২ লাইন এর পরিবর্তে
    
    def post(self, request, *args, **kwargs):
        jason_data = request.body
        stream = io.BytesIO(jason_data)
        python_data = JSONParser().parse(stream)

        serializer = TeacherSerializer( data = python_data )
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data is successfully save in Database.'}
            # json_data = JSONRenderer().render(res)
            # return HttpResponse(json_data, content_type = 'application/json')
            return JsonResponse( res, safe=False ) # উপরের ২ লাইন এর পরিবর্তে
        
        # json_data = JSONRenderer().render(serializer.errors)
        # return HttpResponse(json_data, content_type = 'application/json')
        return JsonResponse( serializer.errors, safe=False ) # উপরের ২ লাইন এর পরিবর্তে
    


    def put(self, request, *args, **kwargs):
        jason_data = request.body
        stream = io.BytesIO(jason_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        teacher =Teacher.objects.get(id = id)

        ## নির্দিষ্ট কিছু Field কে Update করাই হল Partial Update
        serializer = TeacherSerializer( teacher,  data = python_data, partial = True )
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data is successfully Update in Database.'}
            # json_data = JSONRenderer().render(res)
            # return HttpResponse(json_data, content_type = 'application/json')
            return JsonResponse( res, safe=False ) # উপরের ২ লাইন এর পরিবর্তে
        
        # json_data = JSONRenderer().render(serializer.errors)
        # return HttpResponse(json_data, content_type = 'application/json')
        return JsonResponse(serializer.errors, safe=False) # উপরের ২ লাইন এর পরিবর্তে
    


    def delete(self, request, *args, **kwargs):
        jason_data = request.body
        stream = io.BytesIO(jason_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        teacher =Teacher.objects.get(id = id)
        teacher.delete()

        res = {'msg': 'Data Successfully Deleted.'}
        # json_data = JSONRenderer().render(res)
        # return HttpResponse(json_data, content_type = 'application/json')
        return JsonResponse( res, safe=False ) # উপরের ২ লাইন এর পরিবর্তে



