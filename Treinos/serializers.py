from rest_framework import serializers
from .models import Treinos


class TreinoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Treinos
        fields = ['id', 'nomeTreino', 'tempoMinDuracao',
                  'tempoMaxDuracao', 'numeroSeries', 'tipoTreino', 'usuarioId', 'exercicioJson']
