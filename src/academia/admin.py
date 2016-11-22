from django.contrib import admin
from .models import Pessoa

class PessoaAdmin(admin.ModelAdmin):
    search_fields = ['nome', 'data_nasc', 'cpf', 'endereco', 'contato']
    list_display = ('nome', 'data_nasc', 'cpf', 'endereco', 'contato')

# Register your models here.
admin.site.register(Pessoa, PessoaAdmin)
