from re import search
from django.contrib import admin
from .models import PerfilUsuario, Pregunta, ElegirOpcion, PreguntasRespondidas, PerfilUsuario
from .forms import ElegirInlineFormset

class ElegirRespuestaInline(admin.TabularInline):
    model=ElegirOpcion
    can_delete=False
    max_num=ElegirOpcion.maximo_resp
    min_num= ElegirOpcion.maximo_resp
    formset=ElegirInlineFormset

class PreguntaAdmin(admin.ModelAdmin):
    model=Pregunta
    inlines=(ElegirRespuestaInline, )
    list_diplay =['texto',]
    search_files=['texto','preguntas_texto']

class PreguntasRespondidasAdmin(admin.ModelAdmin):
    list_display=['pregunta', 'respuesta', 'correcta', 'puntaje_obtenido']

    class Meta:
        model=PreguntasRespondidas


admin.site.register(Pregunta, PreguntaAdmin)
admin.site.register(ElegirOpcion)
admin.site.register(PreguntasRespondidas)
admin.site.register(PerfilUsuario)