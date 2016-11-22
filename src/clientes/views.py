from datetime import date
from django.shortcuts import render
from .forms import EntradaClienteMF, SaidaClienteMF
from .models import EntradaSaidaCliente


# Create your views here.
def entrada(request):
    entrar = EntradaClienteMF(request.POST or None)
    context = {'entrar': entrar,}
    if entrar.is_valid():
        form_dado = entrar.cleaned_data
        EntradaSaidaCliente.objects.create(cpf=form_dado['cpf'], data_entrada=form_dado['data_entrada'])
        context['ok_message'] = 'Cliente, ' + str(form_dado['cpf']).upper() + ', sua ENTRADA foi autorizada com sucesso! Próximo...'
    return render(request, 'clientes/entrada.html', context)


def saida(request):
    sair = SaidaClienteMF(request.POST or None)
    context = {'sair': sair, }
    if sair.is_valid():
        form_dado = sair.cleaned_data
        try:
            registrado = EntradaSaidaCliente.objects.get(cpf=form_dado['cpf'], data_entrada=date.today())
            registrado.data_saida = registrado.data_entrada
            registrado.save()
            context['ok_message'] = 'Cliente, ' + str(registrado.cpf).upper() + ', sua SAIDA foi autorizada com sucesso! Próximo...'
        except:
            context['error_message'] = 'Cliente nao marcou entrada. Por favor verificar com a Administração!'
    return render(request, 'clientes/saida.html', context)