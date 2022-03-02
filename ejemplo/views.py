from django.shortcuts import render

# Create your views here.

def ejemploa(request):
    return render(request, 'ejemplo/ejemplo1.html')