from django.shortcuts import render, redirect
from app.serializers import StudentSerializer
from app.models import Student

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer


# Create your views here.
