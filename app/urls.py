from django.contrib import admin
from django.urls import path

from app.views import *


urlpatterns = [
    path('display_g_f/', display_function_view, name='display_function_view'),
    path('display_g_c/', display_class_view.as_view(), name='display_class_view'),

    path('display_p_f/', display_function_view_POST, name='display_function_view_POST'),

    path('student-detail/<int:pk>/', student_detail),
]