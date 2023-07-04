from django.contrib import admin
from django.urls import path

from app.views import *


urlpatterns = [
    path('', home, name='home'),

    path('Display_a_data_f/<int:pk>/', Display_a_data_f, name='Display_a_data_f'),
    path('Display_a_data_c/<int:pk>/', Display_a_data_c.as_view(), name='Display_a_data_c'),

    path('Display_all_data_f', Display_all_data_f, name='Display_all_data_f'),
    path('Display_all_data_c', Display_all_data_c.as_view(), name='Display_all_data_c'),

    path('display_g_f/', display_function_view, name='display_function_view'),

    path('create_f/', display_function_view_POST, name='display_function_view_POST'),
    path('create_c/', display_APIView_POST.as_view(), name='display_APIView_POST'),

    path('student_detail/<int:pk>/', student_detail),
]