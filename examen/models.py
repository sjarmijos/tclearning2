from django.db import models
from django.contrib.auth.models import User

import random


class Pregunta(models.Model):
    N_RESP_PERMITIDAS=1
    texto=models.TextField(verbose_name='Texto de la pregunta')
    max_puntaje = models.DecimalField(verbose_name='Maximo puntaje', default=3, decimal_places=2, max_digits=6)
    def __str__(self):
        return self.texto

class ElegirOpcion(models.Model):
    maximo_resp = 4
    pregunta=models.ForeignKey(Pregunta, related_name='opciones', on_delete=models.CASCADE)
    correcta=models.BooleanField(verbose_name='¿es esta la respuesta correcta?', default=False, null=False)
    texto=models.TextField(verbose_name='texto de la respuesta')

    def __str__(self):
        return self.texto

class PerfilUsuario(models.Model):
    usuario=models.OneToOneField(User, on_delete=models.CASCADE)
    puntaje_total=models.DecimalField(verbose_name='Puntaje Total', default=0, decimal_places=2, max_digits=10)

    def crear_intentos(self, pregunta):
        intento=PreguntasRespondidas(pregunta=pregunta, exaUsuario=self)
        intento.save()

    def obtener_nuevas_preguntas(self):
        respondidas=PreguntasRespondidas.objects.filter(exaUsuario=self).values_list('pregunta__pk', flat=True)
        preguntas_restantes=Pregunta.objects.exclude(pk__in=respondidas)
        if not preguntas_restantes.exists():
            return None
        return random.choice(preguntas_restantes)

    def validar_intento(self, pregunta_respondida, respuesta_seleccionada):
        if pregunta_respondida.pregunta_id != respuesta_seleccionada.pregunta_id:
            return
        
        pregunta_respondida.respuesta_selecionada=respuesta_seleccionada
        if respuesta_seleccionada.correcta is True:
            pregunta_respondida.correcta=True
            pregunta_respondida.puntaje_obtenido=respuesta_seleccionada.pregunta.max_puntaje
            pregunta_respondida.respuesta=respuesta_seleccionada
        else:
            pregunta_respondida.respuesta=respuesta_seleccionada

        pregunta_respondida.save()
        self.actualizar_puntaje()

    def actualizar_puntaje(self):
        puntaje_actualizado = self.intentos.filter(correcta=True).aggregate(models.Sum('puntaje_obtenido'))['puntaje_obtenido__sum']

        self.puntaje_total=puntaje_actualizado
        self.save()


class PreguntasRespondidas(models.Model):
    exaUsuario=models.ForeignKey(PerfilUsuario, on_delete=models.CASCADE, related_name='intentos')
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    respuesta=models.ForeignKey(ElegirOpcion, on_delete=models.CASCADE, null=True)
    correcta=models.BooleanField(verbose_name='¿Es esta la respuesta correcta?', default=False, null=False)
    puntaje_obtenido=models.DecimalField(verbose_name='Puntaje Objetido', default=0, decimal_places=2, max_digits=6)

