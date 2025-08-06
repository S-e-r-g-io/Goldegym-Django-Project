from django.db import models

# Create your models here.
class Cliente(models.Model):
    codice = models.IntegerField()
    nome = models.CharField(max_length=20)
    cognome = models.CharField(max_length=40)
    cf = models.CharField(max_length=16)
    indirizzo = models.TextField()
    tel = models.CharField(max_length=20)
    email = models.EmailField()
    dataNas = models.DateField()