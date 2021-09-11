from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import Usuario
import re


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = Usuario.objects.create(email=validated_data['email'],
                                      username=validated_data['username'],
                                      password=make_password(validated_data['password']))
        return user

    def check_password(self, validated_data):
        password = make_password(validated_data)
        user = Usuario.objects.filter(password=password).exists()
        return user
