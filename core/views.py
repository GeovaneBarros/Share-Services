from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import *
from .models import *
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import status


class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer


class DescricaoViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Descricao.objects.all()
    serializer_class = DescricaoSerializers

class EnderecoViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer

class ContatoViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Contato.objects.all()
    serializer_class = ContatoSerializer
