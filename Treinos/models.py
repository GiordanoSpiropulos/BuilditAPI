from Usuario.models import Usuario
from django.db import models
from django.db.models.fields import PositiveIntegerField


def upload_to_image(instance, filename):
    return 'treino/' + f"{instance.id}-{filename}"


class Treino(models.Model):
    id = models.BigAutoField(primary_key=True)
    usuarioId = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    nomeTreino = models.CharField(max_length=255)
    tempoMinDuracao = models.CharField(max_length=255, null=True,)
    numeroSeries = PositiveIntegerField()
    tipoTreino = PositiveIntegerField(default=0)
    exercicioJson = models.JSONField()
    image = models.ImageField(upload_to=upload_to_image, blank=True, null=True)
