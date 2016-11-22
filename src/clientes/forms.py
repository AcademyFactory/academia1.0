from django import forms
from .models import EntradaSaidaCliente

class EntradaClienteMF(forms.ModelForm):
    class Meta:
        model = EntradaSaidaCliente
        fields = ('cpf', 'data_entrada')


class SaidaClienteMF(forms.ModelForm):
    class Meta:
        model = EntradaSaidaCliente
        fields = ('cpf',)

