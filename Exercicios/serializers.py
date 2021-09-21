from rest_framework import serializers
from .models import Exercicios


class ExercicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercicios
        fields = ['id', 'nomeExercicio']
