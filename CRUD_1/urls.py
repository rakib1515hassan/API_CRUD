from django.contrib import admin
from django.urls import path

from CRUD_1.views import *


urlpatterns = [
    path('teacher_crud_api/', teacher_crud_api),
    path('Teacher_crud_classApiView/', Teacher_crud_classApiView.as_view()),

]