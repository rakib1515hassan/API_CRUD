from django.contrib import admin
from django.urls import path

from CRUD_app.views import *


urlpatterns = [
    path('teacher_crud_api/', teacher_crud_api),

]