# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-22 03:02
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('academia', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EntradaSaidaFuncionario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_entrada', models.DateField(default=datetime.date.today, verbose_name='Data de Entrada')),
                ('data_saida', models.DateField(blank=True, null=True, verbose_name='Data de Saída')),
            ],
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salario', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Salário')),
                ('cpf', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='academia.Pessoa', verbose_name='Funcionarios - CPF')),
            ],
        ),
        migrations.CreateModel(
            name='PagarFuncionario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_pagamento', models.DateField(verbose_name='Data de Pagamento')),
                ('confirmacao', models.BooleanField()),
                ('cpf', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='funcionarios.Funcionario', unique_for_month='data_pagamento', verbose_name='CPF')),
            ],
        ),
        migrations.AddField(
            model_name='entradasaidafuncionario',
            name='cpf',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='funcionarios.Funcionario', unique_for_date='data_entrada'),
        ),
    ]
