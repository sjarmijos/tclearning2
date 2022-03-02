from django.http import request
from django.urls import path
from .views import *

urlpatterns=[
    path('conjuntos/', conjunto, name='Tconjuntos'),
    path('operaciones/', operacion, name='Toperaciones'),
    path('algebra/', algebra, name='Talgebra'),
]