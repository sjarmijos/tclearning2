from django.urls import path
from .views import *

urlpatterns=[
    path('videosejm/', videos, name="ejmvideo"),
]