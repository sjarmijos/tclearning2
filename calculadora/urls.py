from django.urls import path
from .views import *

urlpatterns=[
    path('menu/', menucalc, name="menucalc"),
    path('', calc, name="calculadora"),
    path('add/', union, name="add"),
    path('inter/', intersec, name="inter"),
    path('ci/', calcinter,name="calcuinter"),
    path('cd/', calcdif, name="calcudif"), 
    path('dif/', dif, name="dife"),
    path('cdsim/', calcdsim, name="calcudifsim"),
    path('dsim/', difsim, name="dsim"),
]