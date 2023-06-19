from django.contrib import admin
from django.urls import path

from app.views import *
# from ApiNote.views import note
from .views import *


urlpatterns = [
    path('introduction/', introduction, name='introduction'),
    path('serialization/', serialization, name='serialization'),
    path('de_serialization/', de_serialization, name='de_serialization'),

]