from django.contrib import admin
from .models import *


class FuncionarioAdmin(admin.ModelAdmin):
    search_fields = ['cpf', 'salario']
    list_display = ('cpf', 'salario')


class PagarFuncionarioAdmin(admin.ModelAdmin):
    search_fields = ['cpf', 'data_pagamento']
    list_display = ('cpf', 'data_pagamento', 'confirmacao')


class EntradaSaidaFuncionarioAdmin(admin.ModelAdmin):
    list_display = ('cpf', 'data_entrada', 'data_saida')

# Register your models here.
admin.site.register(Funcionario, FuncionarioAdmin)
admin.site.register(PagarFuncionario, PagarFuncionarioAdmin)
admin.site.register(EntradaSaidaFuncionario, EntradaSaidaFuncionarioAdmin)
