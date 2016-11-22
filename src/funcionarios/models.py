# Create your models here.
from django.db import models
from academia.models import Pessoa
import datetime


# Create your models here.
class Funcionario(models.Model):
    salario = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Salário')
    cpf = models.OneToOneField(Pessoa, verbose_name='Funcionarios - CPF')

    def __str__(self):
        return str(self.cpf)


class PagarFuncionario(models.Model):
    cpf = models.ForeignKey(Funcionario, unique_for_month='data_pagamento', verbose_name='CPF', on_delete=models.PROTECT)
    data_pagamento = models.DateField(verbose_name='Data de Pagamento')
    confirmacao = models.BooleanField()

    def __str__(self):
        return str(self.cpf)

class EntradaSaidaFuncionario(models.Model):
    data_entrada = models.DateField(default=datetime.date.today, verbose_name='Data de Entrada')
    data_saida = models.DateField(blank=True, null=True, verbose_name='Data de Saída')
    cpf = models.ForeignKey(Funcionario, unique_for_date='data_entrada', on_delete=models.PROTECT)

    def __str__(self):
        return str(self.cpf)
