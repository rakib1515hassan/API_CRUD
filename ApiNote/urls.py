from django.contrib import admin
from django.urls import path

from ApiNote.views import *


urlpatterns = [
    path('introduction/', introduction, name='introduction'),
    path('serialization/', serialization, name='serialization'),
    path('de_serialization/', de_serialization, name='de_serialization'),

    path('3rd-parti-api/', a_3rd_parti_api__post_request_test, name='a_3rd_parti_api__post_request_test'),

]