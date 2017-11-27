# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-27 21:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20171127_1816'),
    ]

    operations = [
        migrations.CreateModel(
            name='Questao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_limite', models.DateField(verbose_name='Data Limite')),
                ('descricao', models.TextField(verbose_name='Descricao')),
                ('data', models.DateField(verbose_name='Data')),
                ('disciplina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Disciplina')),
                ('disciplinaofertada', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.DisciplinaOfertada')),
                ('turma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Turma')),
            ],
        ),
        migrations.CreateModel(
            name='Resposta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disciplina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Disciplina')),
                ('disciplinaofertada', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.DisciplinaOfertada')),
                ('questao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Questao')),
                ('turma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Turma')),
            ],
        ),
    ]
