
from django.shortcuts import render
# Create your views here.
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.core.exceptions import ObjectDoesNotExist

from .models import PerfilUsuario, Pregunta, PreguntasRespondidas
# Create your views here.


def tablero(request):
    total_usuarios_exa = PerfilUsuario.objects.order_by('-puntaje_total')
    contador = total_usuarios_exa.count
    return render(request, 'examen/puntajes.html',{
        'usuario_exa':total_usuarios_exa,
        'Tusuarios': contador,
    })

def jugar(request):
    if request.user.is_authenticated:
        exaUsuario, created= PerfilUsuario.objects.get_or_create(usuario=request.user)
        if request.method == 'POST':
            pregunta_pk= request.POST.get('pregunta_pk')
            pregunta_respondida = exaUsuario.intentos.select_related('pregunta').get(pregunta__pk=pregunta_pk)
            respuesta_pk=request.POST.get('respuesta_pk')
            
            try:
                opcion_seleccionada=pregunta_respondida.pregunta.opciones.get(pk=respuesta_pk)
            except ObjectDoesNotExist:
                return redirect('resultado', pregunta_respondida.pk)

            exaUsuario.validar_intento(pregunta_respondida, opcion_seleccionada)
            return redirect('resultado',pregunta_respondida.pk)

        else:
            pregunta=exaUsuario.obtener_nuevas_preguntas()
            if pregunta is not None:
                exaUsuario.crear_intentos(pregunta)

        return render(request, 'examen/jugar.html', {
            'pregunta':pregunta
        })
    else:
        txt='Inicio de Sesión Obligatorio'
        return render(request,'examen/jugar.html', {
            'error':txt
        })

def reset_juego(request):
    registros_pr=PreguntasRespondidas.objects.all()
    registros_pr.delete()
    registros_pu=PerfilUsuario.objects.all()
    registros_pu.delete()
    return render(request, 'gestion/land.html')

def resultado_pregunta(request, pregunta_respondida_pk):
    respondida=get_object_or_404(PreguntasRespondidas, pk=pregunta_respondida_pk)

    return render(request, 'examen/resultado.html', {
        'respondida':respondida,
    })
