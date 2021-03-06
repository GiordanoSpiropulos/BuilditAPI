# Generated by Django 3.2.7 on 2021-09-23 00:20

import Exercicios.models
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exercicio',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nomeExercicio', models.TextField(max_length=255)),
                ('image', models.ImageField(blank=True, null=True, upload_to=Exercicios.models.upload_to_image)),
                ('deleted', models.BooleanField(default=False)),
            ],
        ),
    ]
