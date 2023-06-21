from django.contrib import admin
from django.urls import path

from CRUD_2.views import *


urlpatterns = [
    path('teacher_crud_api/', teacher_crud_api),
    path('teacher_crud_api/<int:pk>/', teacher_crud_api),

    # path('Teacher_crud_classApiView/', Teacher_crud_classApiView.as_view()),

]