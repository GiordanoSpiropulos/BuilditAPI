# Generated by Django 3.2.7 on 2021-09-18 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Treinos', '0002_treinos_usuarioid'),
    ]

    operations = [
        migrations.AddField(
            model_name='treinos',
            name='exercicioJson',
            field=models.JSONField(default=None),
            preserve_default=False,
        ),
    ]
