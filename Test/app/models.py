""" Modelos de la aplicación  """
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Persona(models.Model):
    SEX_CHOICES = (
        ('Masculino', 'Masculino'),
        ('Feminino', 'Feminino'),
    )

    Name = models.CharField(max_length=100, blank=True)
    PathernalLastName = models.CharField(max_length=100, blank=True)
    MathernalLastName = models.CharField(max_length=100, blank=True)
    Edad = models.IntegerField(blank=True, default=0)
    Cedula = models.CharField(max_length=20, blank=True)
    Sexo = models.CharField(max_length=100, choices =SEX_CHOICES)
  

    def __str__(self):
        return self.Name


class Email(models.Model):

    persona = models.ForeignKey('persona', on_delete=models.CASCADE)
    Email = models.CharField(max_length=100, blank=True)
    Orden = models.IntegerField(default=0)

    class Meta:
        ordering  = ['Orden']

    def __str__(self):
        return self.Email