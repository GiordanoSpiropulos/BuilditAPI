# Generated by Django 3.2.7 on 2021-09-23 00:20

import Treinos.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Treino',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('nomeTreino', models.CharField(max_length=255, unique=True)),
                ('tempoMinDuracao', models.PositiveIntegerField(null=True)),
                ('tempoMaxDuracao', models.PositiveIntegerField(null=True)),
                ('numeroSeries', models.PositiveIntegerField()),
                ('tipoTreino', models.PositiveIntegerField()),
                ('exercicioJson', models.JSONField()),
                ('image', models.ImageField(blank=True, null=True, upload_to=Treinos.models.upload_to_image)),
                ('deleted', models.BooleanField(default=False)),
            ],
        ),
    ]
