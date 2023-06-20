from django.shortcuts import render, redirect
import io
from rest_framework.parsers import JSONParser
from app.serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def introduction(request):
    return render(request, 'Note/introduction.html')


def serialization(request):
    return render(request, 'Note/serialization.html')



def de_serialization(request):
    return render(request, 'Note/de_serialization.html')



# URL = ( http://127.0.0.1:8000/3rd-parti-api/ )
@csrf_exempt
def a_3rd_parti_api__post_request_test(request):
    if request.method == "POST":
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializar = StudentSerializer(data = python_data)

        if serializar.is_valid():
            serializar.save()
            res_ponce = {'msg': 'Data is successfully save in Database.'}

            json_data = JSONRenderer().render(res_ponce)
            return HttpResponse(json_data, content_type = 'application/json')
            # return JsonResponse(serializar.data) # উপরের ২ লাইন এর পরিবর্তে আমরা JsonResponse ব্যবহার করতে পারি
        
        json_data = JSONRenderer().render(serializar.errors)
        return HttpResponse(json_data, content_type = 'application/json')
        # return JsonResponse(serializar.data) # উপরের ২ লাইন এর পরিবর্তে আমরা JsonResponse ব্যবহার করতে পারি