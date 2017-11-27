# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-27 18:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20171023_2146'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ra', models.IntegerField(verbose_name='RA Aluno')),
                ('nome', models.CharField(max_length=120, verbose_name='Nome')),
                ('email', models.CharField(max_length=80, verbose_name='E-Mail')),
                ('celular', models.CharField(max_length=11, verbose_name='Celular')),
                ('id_curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Curso')),
            ],
        ),
    ]
