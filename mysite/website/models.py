from django.db import models

# Create your models here.
class Cliente(models.Model):
    nome = models.CharField(max_length=120)
    cognome = models.TextField(blank=True, null=True)
    cf = models.TextField(default="0")
