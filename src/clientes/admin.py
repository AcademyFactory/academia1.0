from django.contrib import admin
from .models import *


class ClienteAdmin(admin.ModelAdmin):
    search_fields = ['cpf', 'mensalidade']
    list_display = ('cpf', 'mensalidade', 'dia_mensalidade')


class ReceberMensalidadeAdmin(admin.ModelAdmin):
    search_fields = ['cpf', 'data_recebimento']
    list_display = ('cpf', 'data_recebimento', 'confirmacao')


class EntradaSaidaClienteAdmin(admin.ModelAdmin):
    list_display = ('cpf', 'data_entrada', 'data_saida')


# Register your models here.
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(ReceberMensalidade, ReceberMensalidadeAdmin)
admin.site.register(EntradaSaidaCliente, EntradaSaidaClienteAdmin)