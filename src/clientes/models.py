from django.db import models
from academia.models import Pessoa
import datetime


# Create your models here.
class Cliente(models.Model):
    mensalidade = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Mensalidade')
    dia_mensalidade = models.IntegerField(verbose_name='Dia da Mensalidade')
    cpf = models.OneToOneField(Pessoa, verbose_name='Cliente - CPF')

    def __str__(self):
        return str(self.cpf)


class ReceberMensalidade(models.Model):
    cpf = models.ForeignKey(Cliente, unique_for_month='data_recebimento', verbose_name='CPF', on_delete=models.PROTECT)
    data_recebimento = models.DateField(verbose_name='Data de Recebimento')
    confirmacao = models.BooleanField()

    def __str__(self):
        return str(self.cpf)


class EntradaSaidaCliente(models.Model):
    data_entrada = models.DateField(default=datetime.date.today, verbose_name='Data de Entrada')
    data_saida = models.DateField(blank=True, null=True, verbose_name='Data de Saída')
    cpf = models.ForeignKey(Cliente, unique_for_date='data_entrada', on_delete=models.PROTECT)

    def __str__(self):
        return str(self.cpf)
