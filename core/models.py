from django.db import models
from django.contrib.auth.models import User

class Contato(models.Model):
    celular = models.CharField(max_length=16)
    telefone = models.CharField(max_length=16, null=True)
    email = models.EmailField(max_length=64)

    class Meta:
        verbose_name = "Contato"
        verbose_name_plural = "Contatos"
    
    def __str__(self):
        return self.celular

class Endereco(models.Model):
    rua = models.CharField(max_length=64)
    numero = models.CharField(max_length=8)
    bairro = models.CharField(max_length=32)
    cidade = models.CharField(max_length=32)

    class Meta:
        verbose_name = "Endereço"
        verbose_name_plural = "Endereços"
    def __str__(self):
        return ("Rua: {} Número: {} Bairro: {}".format(self.rua,self.bairro,self.cidade))


class Empresa(models.Model):
    nome = models.CharField(max_length=100)
    ramo = models.CharField(max_length=100)
    foto = models.ImageField(null=True, blank=True)
    cnpj = models.CharField(max_length=20, blank=True, null=True)
    contato = models.OneToOneField(Contato, on_delete=models.CASCADE, null = True, blank=True)
    endereco = models.OneToOneField(Endereco, on_delete=models.CASCADE, null = True, blank=True) 
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    premium = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'

    def __str__(self):
        return '{} {}'.format(self.ramo, self.nome)

class Descricao(models.Model):
    servicos = models.CharField(max_length=1024)
    produtos = models.CharField(max_length=1024)
    historia = models.CharField(max_length=512)
    empresa = models.OneToOneField(Empresa, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Descrição'
        verbose_name_plural = 'Descrições'
    