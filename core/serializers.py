from rest_framework import serializers
from .models import Prestador, Contato, Endereco, Cliente, Avaliacao
from django.contrib.auth.models import User

class PrestadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prestador
        fields = ['nome', 'profissao', 'ponto', 'ateCliente', 'contato', 'endereco']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class ContatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contato
        fields = '__all__'

class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = '__all__'

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['nome', 'sobrenome', 'contato', 'endereco']

class AvaliacaoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Avaliacao
        fields = ['nota', 'comentario', 'prestador', 'anonimo']