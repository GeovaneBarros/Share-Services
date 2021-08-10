from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


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

class EmpresaSerializer(serializers.ModelSerializer):
    usuario = UserSerializer(write_only = True)

    class Meta:
        model = Empresa
        exclude = ['user']

    def create(self, validated_data):
        usuario = validated_data['usuario']
        
        email = usuario['email']
        username = usuario['username']
        password = usuario['password']
        
        user = User(
            email=email,
            username=username
        )
        user.set_password(password)
        user.save()

        empresa = Empresa(
            nome = validated_data['nome'],
            ramo = validated_data['ramo'],
            user = user
        )

        empresa.save()
        return empresa

class ContatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contato
        fields = '__all__'

class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = '__all__'

class DescricaoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Descricao
        fields = '__all__'