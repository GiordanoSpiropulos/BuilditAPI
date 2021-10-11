from rest_framework import serializers
from .models import Treino


class TreinoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Treino
        fields = ['id', 'nomeTreino', 'tempoMinDuracao', 'numeroSeries',
                  'tipoTreino', 'usuarioId', 'exercicioJson', 'image']
