from django import forms
from .models import EntradaSaidaFuncionario

class EntradaFuncionarioMF(forms.ModelForm):
    class Meta:
        model = EntradaSaidaFuncionario
        fields = ('cpf', 'data_entrada')


class SaidaFuncionarioMF(forms.ModelForm):
    class Meta:
        model = EntradaSaidaFuncionario
        fields = ('cpf',)

