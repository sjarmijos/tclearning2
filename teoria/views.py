from django.shortcuts import render

# Create your views here.

def conjunto(request):
    return render(request, 'teoria/conjunto.html')

def operacion(request):
    return render(request, 'teoria/operaciones.html')

def algebra(request):
    return render(request, 'teoria/algebra.html')