from django.db import models

# Create your models here.
#MCF(Meu carro favorito)
class MCF(models.Model):
  marca = models.CharField(max_length=100)
  modelo = models.CharField(max_length=40)
  ano=models.DateField()

#RCV(Ranking maior qtd cavalos)
class RCV(models.Model):
  marca = models.CharField(max_length=40)
  modelo = models.CharField(max_length=40)
  ano = models.DateField()
  potencia = models.IntegerField()
  cv = models.CharField(max_length=3)