from django.db import models
from django.contrib.auth.models import User

# Create your models here.
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


class Prestador(models.Model):
    nome = models.CharField(max_length=100)
    profissao = models.CharField(max_length=100)
    ponto = models.BooleanField()
    ateCliente = models.BooleanField()
    diferencial = models.CharField(max_length=256)
    contato = models.OneToOneField(Contato, on_delete=models.CASCADE, null = True)
    endereco = models.OneToOneField(Endereco, on_delete=models.CASCADE, null = True) 
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Prestador de serviço'
        verbose_name_plural = 'Prestadores de serviço'

    def __str__(self):
        return '{} {}'.format(self.profissao, self.nome)

class Servico(models.Model):
    nome = models.CharField(max_length = 64)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.CharField(max_length=256)
    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

    def __str__(self):
        return '{} {}'.format(self.nome, self.preco)

class Cliente(models.Model):
    nome = models.CharField(max_length = 64)
    sobrenome = models.CharField(max_length = 64)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contato = models.OneToOneField(Contato, on_delete=models.CASCADE, null = True)
    endereco = models.OneToOneField(Endereco, on_delete=models.CASCADE, null = True)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return '{} {}'.format(self.nome, self.sobrenome)


class Avaliacao(models.Model):
    nota = models.PositiveSmallIntegerField(null=True)
    comentario = models.CharField(max_length=256)
    anonimo = models.BooleanField(default=False)
    prestador = models.ForeignKey(Prestador, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Avaliação'
        verbose_name_plural = 'Avaliações'
    
    def __str__(self):
        return '{}: {}'.format(self.nota, self.comentario)