from django.http import request
from django.urls import path
from .views import *

urlpatterns=[
    path('Cbasico/', ejemploa, name="Ebasico"),
]