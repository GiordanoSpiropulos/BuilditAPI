
from django.db import models

# Create your models here.


class Exercicios(models.Model):
    nomeExercicio = models.TextField(max_length=255)
