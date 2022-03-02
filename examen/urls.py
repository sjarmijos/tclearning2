from django.urls import path
from .views import *

urlpatterns=[
    path('jugar/', jugar, name='jugar'),
    path('resultado/<int:pregunta_respondida_pk>', resultado_pregunta, name='resultado'),
    path('puntajes/', tablero, name='puntajes'),
    path('reset/', reset_juego, name='reset'),
]