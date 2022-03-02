
from django.shortcuts import render
from .utils import get_dif, get_difsim, get_inter, get_plot

# Create your views here.

def menucalc(request):
    return render(request, 'calculadora/menu.html')

def calc(request):
    return render(request, 'calculadora/form.html')

def calcinter(request):
    return render(request, 'calculadora/form2.html')

def calcdif(request):
    return render(request, 'calculadora/form3.html')

def calcdsim(request):
    return render(request, 'calculadora/form4.html')



def union(request):

    cja=set()
    cjb=set()

    try:
        conjA = request.GET['c1'].replace(' ', '')
        conjB = request.GET['c2'].replace(' ', '')
        cja = {int(n) for n in conjA.split(",")}
        cjb = {int(n) for n in conjB.split(",")}
    except ValueError:
        txt="Los datos ingresados en los conjuntos están incorrectos, recuerde que despues de cada numero se coloca una sola coma ejemplo: 1,2,3,4,5 adicionalmente asegurese de que no existen comas al inicio o al final del conjunto ingresado ejemplo: ,1,2,3,"
        return render(request, 'calculadora/form.html', {
            "error":txt,
        })

    
        
    unionr=cja | cjb

    x=cja-cjb
    y=cja&cjb
    z=cjb-cja
    chart = get_plot(x, y, z)

    return render(request, 'calculadora/union.html', {
        "ca": cja,
        "cb": cjb,
        "resultado":unionr, 
        "chart":chart,
    })

def intersec(request):
    cja=set()
    cjb=set()

    try:
        conjA = request.GET['c1'].replace(' ', '')
        conjB = request.GET['c2'].replace(' ', '')
        cja = {int(n) for n in conjA.split(",")}
        cjb = {int(n) for n in conjB.split(",")}
    except ValueError:
        txt="Los datos ingresados en los conjuntos están incorrectos, recuerde que despues de cada numero se coloca una sola coma ejemplo: 1,2,3,4,5 adicionalmente asegurese de que no existen comas al inicio o al final del conjunto ingresado ejemplo: ,1,2,3,"
        return render(request, 'calculadora/form2.html', {
            "error":txt,
        })

    res=cja&cjb
    x=cja-cjb
    y=cja&cjb
    z=cjb-cja
    chart =get_inter(x,y,z)
    

    return render(request, 'calculadora/interseccion.html', {
        "ca": cja,
        "cb": cjb,
        "resultado":res, 
        "chart":chart,
    })

def dif(request):
    cja=set()
    cjb=set()

    try:
        conjA = request.GET['c1'].replace(' ', '')
        conjB = request.GET['c2'].replace(' ', '')
        cja = {int(n) for n in conjA.split(",")}
        cjb = {int(n) for n in conjB.split(",")}
    except ValueError:
        txt="Los datos ingresados en los conjuntos están incorrectos, recuerde que despues de cada numero se coloca una sola coma ejemplo: 1,2,3,4,5 adicionalmente asegurese de que no existen comas al inicio o al final del conjunto ingresado ejemplo: ,1,2,3,"
        return render(request, 'calculadora/form3.html', {
            "error":txt,
        })

    res=cjb-cja
    x=cja-cjb
    y=cja&cjb
    z=cjb-cja
    chartd = get_dif (x,y,z)
    

    return render(request, 'calculadora/diferencia.html', {
        "ca": cja,
        "cb": cjb,
        "resultado1":x,
        "resultado2":res, 
        "chart":chartd,
    })

def difsim(request):
    cja=set()
    cjb=set()
    try:
        conjA = request.GET['c1'].replace(' ', '')
        conjB = request.GET['c2'].replace(' ', '')
        cja = {int(n) for n in conjA.split(",")}
        cjb = {int(n) for n in conjB.split(",")}
    except ValueError:
        txt="Los datos ingresados en los conjuntos están incorrectos, recuerde que despues de cada numero se coloca una sola coma ejemplo: 1,2,3,4,5 adicionalmente asegurese de que no existen comas al inicio o al final del conjunto ingresado ejemplo: ,1,2,3,"
        return render(request, 'calculadora/form4.html', {
            "error":txt,
        })

    res=cja^cjb
    x=cja-cjb
    y=cja&cjb
    z=cjb-cja
    chart = get_difsim(x,y,z)
    

    return render(request, 'calculadora/simetrica.html', {
        "ca": cja,
        "cb": cjb,
        "resultado":res, 
        "chart":chart,
    })