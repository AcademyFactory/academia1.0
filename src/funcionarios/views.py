from datetime import date
from django.shortcuts import render
from .forms import EntradaFuncionarioMF, SaidaFuncionarioMF
from .models import EntradaSaidaFuncionario


# Create your views here.
def entrada(request):
    entrar = EntradaFuncionarioMF(request.POST or None)
    context = {'entrar': entrar,}
    if entrar.is_valid():
        form_dado = entrar.cleaned_data
        EntradaSaidaFuncionario.objects.create(cpf=form_dado['cpf'], data_entrada=form_dado['data_entrada'])
        context['ok_message'] = 'Funcionaria(o), ' + str( form_dado['cpf']).upper() + ', sua ENTRADA foi autorizada com sucesso! Próximo...'
    return render(request, 'funcionarios/entrada.html', context)


def saida(request):
    sair = SaidaFuncionarioMF(request.POST or None)
    context = {'sair': sair,}
    if sair.is_valid():
        form_dado = sair.cleaned_data
        try:
            registrado = EntradaSaidaFuncionario.objects.get(cpf=form_dado['cpf'], data_entrada=date.today())
            registrado.data_saida = registrado.data_entrada
            registrado.save()
            context['ok_message'] = 'Funcionaria(o), ' + str(registrado.cpf).upper() + ', sua SAIDA foi autorizada com sucesso! Próximo...'
        except:
            context['error_message'] = 'Funcionario nao marcou entrada. Por favor verificar com a Administração!'
    return render(request, 'funcionarios/saida.html', context)