from Usuario.models import Usuario
from django.db import models
from django.db.models.fields import PositiveIntegerField


# Create your models here.

class Treinos(models.Model):
    usuarioId = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    nomeTreino = models.CharField(max_length=255, unique=True)
    tempoMinDuracao = models.PositiveIntegerField(null=True)
    tempoMaxDuracao = PositiveIntegerField(null=True)
    numeroSeries = PositiveIntegerField()
    tipoTreino = PositiveIntegerField()
    exercicioJson = models.JSONField()

    def __str__(self):
        return self.nomeTreino
