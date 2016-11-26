from django import forms


class Logar(forms.Form):
    login = forms.CharField(max_length=20)
    senha = forms.CharField(max_length=20)