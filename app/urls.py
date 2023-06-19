from django.contrib import admin
from django.urls import path

from app.views import *


urlpatterns = [
    path('', home, name='home'),

    path('Display_a_data_f/<int:pk>/', Display_a_data_f, name='Display_a_data_f'),
    # path('students/<int:pk>/', DisplayDataAPIView.as_view(), name='display-data'),

    path('Display_all_data_f', Display_all_data_f, name='Display_all_data_f'),




    path('display_g_f/', display_function_view, name='display_function_view'),
    path('display_g_c/', display_class_view.as_view(), name='display_class_view'),

    path('display_p_f/', display_function_view_POST, name='display_function_view_POST'),

    path('student_detail/<int:pk>/', student_detail),
]