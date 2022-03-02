from django import forms
from .models import Pregunta, ElegirOpcion, PreguntasRespondidas


from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model, authenticate

User=get_user_model()

class ElegirInlineFormset(forms.BaseInlineFormSet):
    def clean(self):
        super(ElegirInlineFormset, self).clean()

        respuesta_correcta=0
        for formulario in self.forms:
            if not formulario.is_valid():
                return 
            
            if formulario.cleaned_data and formulario.cleaned_data.get('correcta') is True:
                respuesta_correcta += 1

        try:
            assert respuesta_correcta == Pregunta.N_RESP_PERMITIDAS
        except AssertionError:
            raise forms.ValidationError('Solo se permite una sola respuesta correcta')