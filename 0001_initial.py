# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id_categoria', models.AutoField(serialize=False, primary_key=True)),
                ('dispo_legal', models.CharField(max_length=100)),
                ('ley', models.CharField(max_length=10)),
                ('articulo', models.IntegerField()),
                ('inciso', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'categoria',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Infraccion',
            fields=[
                ('id_infraccion', models.AutoField(serialize=False, primary_key=True)),
                ('dispo_legal', models.CharField(max_length=100)),
                ('ley', models.IntegerField()),
                ('articulo', models.CharField(max_length=30)),
                ('inciso', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'infraccion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Infractor',
            fields=[
                ('id_inf', models.AutoField(serialize=False, primary_key=True)),
                ('dni', models.IntegerField()),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('sexo', models.CharField(max_length=1)),
                ('domicilio', models.CharField(max_length=250)),
                ('localidad', models.CharField(max_length=50)),
                ('provincia', models.CharField(max_length=50)),
                ('pais', models.CharField(max_length=30)),
                ('cod_postal', models.IntegerField()),
                ('licencia', models.CharField(max_length=15)),
                ('clase', models.CharField(max_length=5)),
                ('vence', models.DateField()),
            ],
            options={
                'db_table': 'infractor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Medicion',
            fields=[
                ('id_al', models.AutoField(serialize=False, primary_key=True)),
                ('marca', models.CharField(max_length=30)),
                ('modelo', models.CharField(max_length=30)),
                ('nro_serie', models.CharField(max_length=30)),
                ('cod_aprobacion', models.IntegerField()),
                ('valor', models.DecimalField(max_digits=3, decimal_places=0)),
            ],
            options={
                'db_table': 'medicion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Multa',
            fields=[
                ('id_multa', models.AutoField(serialize=False, primary_key=True)),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
                ('id_infractor', models.IntegerField()),
                ('id_usuario', models.IntegerField()),
                ('id_vehiculo', models.IntegerField()),
                ('id_infraccion', models.IntegerField()),
                ('partido', models.CharField(max_length=30)),
                ('localidad', models.CharField(max_length=30)),
                ('direccion', models.CharField(max_length=60)),
                ('circulacion', models.CharField(max_length=12)),
                ('retuvo_licencia', models.IntegerField()),
                ('retuvo_vehiculo', models.IntegerField()),
                ('observaciones', models.TextField()),
            ],
            options={
                'db_table': 'multa',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dni', models.IntegerField()),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=30)),
                ('fech_nac', models.DateField()),
                ('cel', models.IntegerField()),
                ('us', models.CharField(max_length=20)),
                ('pass_field', models.CharField(max_length=15, db_column=b'pass')),
            ],
            options={
                'db_table': 'usuario',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id_vehiculo', models.AutoField(serialize=False, primary_key=True)),
                ('dominio', models.CharField(max_length=8)),
                ('propietario', models.CharField(max_length=60)),
                ('dni_propietario', models.IntegerField()),
                ('marca', models.CharField(max_length=20)),
                ('color', models.CharField(max_length=20)),
                ('modelo', models.IntegerField()),
                ('tipo', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'vehiculo',
                'managed': False,
            },
        ),
    ]
