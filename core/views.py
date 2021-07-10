from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from .serializers import UserSerializer, PrestadorSerializer, ContatoSerializer, EnderecoSerializer, ClienteSerializer, AvaliacaoSerializers
from .models import Prestador, Contato, Endereco, Cliente, Avaliacao
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404


# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PrestadorViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Prestador.objects.all()
    serializer_class = PrestadorSerializer
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class EnderecoViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer

class ContatoViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Contato.objects.all()
    serializer_class = ContatoSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class AvaliacaoViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializers
    
    def create(self, serializer):
        try:
            cliente = Cliente.objects.get(user=self.request.user)
            serializer.save(cliente = cliente)
        except Cliente.DoesNotExist:
            response = Response({'Cliente does not exist'}, status=status.HTTP_400_BAD_REQUEST)
            return response