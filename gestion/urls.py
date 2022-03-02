from django.urls import path
from .views import *

urlpatterns=[
    path('', indexL, name="indexLand"),
    path('inicio/', indexH, name="indexInicio"),
]