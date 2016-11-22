from django.db import models

# Create your models here.
class Pessoa(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome')
    cpf = models.CharField(primary_key=True, max_length=14, verbose_name='Pessoa - CPF')
    data_nasc = models.DateField(verbose_name='Data de Nascimento')
    endereco = models.CharField(max_length=100, verbose_name='Endereço')
    contato = models.CharField(max_length=16, verbose_name='Contato')

    def __str__(self):
        return self.nome