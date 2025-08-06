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

class Abbonamento(models.Model):
    nAbb = models.IntegerField()
    cliente = models.IntegerField()
    inizio = models.DateField()
    fine = models.DateField()
    prezzo = models.DecimalField(max_digits=5, decimal_places=2)

class FasciaOraria(models.Model):
    sala = models.IntegerField()
    data = models.DateField()
    ora = models.TimeField()
    durata = models.IntegerField()

class Sala(models.Model):
    codice = models.IntegerField()
    nome = models.CharField(max_length=20)
    tema = models.TextField()
    mq = models.DecimalField(max_digits=5, decimal_places=2)

class Posto(models.Model):
    sala = models.IntegerField()
    data = models.DateField()
    ora = models.TimeField()
    nProg = models.IntegerField()

class Prenotazione(models.Model):
    nProg = models.IntegerField()
    cliente = models.IntegerField()
    sala = models.IntegerField()
    data = models.DateField()
    ora = models.TimeField()
    posto = models.IntegerField()

class SubAbbonamento(models.Model):
    prenotazione = models.IntegerField()
    abbonamento = models.IntegerField()