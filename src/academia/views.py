from django.shortcuts import render
from .forms import *


# Create your views here.
def login(request):
    entrar = Logar(request.POST or None)
    context = {'entrar': entrar,}
    if entrar.is_valid():
        form_dado = entrar.cleaned_data
        loginForm = form_dado['login']
        senhaForm = form_dado['senha']

        if loginForm == 'admin' and senhaForm == 'admin123':
            ok = True
            context['ok'] = ok
            return render(request, 'academia/ponto.html', context)
    return render(request, 'academia/login.html', context)
