# Generated by Django 3.2.7 on 2021-09-23 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Exercicios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercicio',
            name='descricao',
            field=models.TextField(default=None, max_length=1000),
            preserve_default=False,
        ),
    ]
