from django.db import models

# Create your models here.

class Futbol(models.Model):
    apellido = models.CharField(max_length=256)
    nombre = models.CharField(max_length=256)
    email = models.EmailField(blank=True)
    dni = models.CharField(max_length=32)
    telefono = models.CharField(max_length=20, blank=True)

    
class Basquet(models.Model):
    apellido = models.CharField(max_length=256)
    nombre = models.CharField(max_length=256)
    email = models.EmailField(blank=True)
    dni = models.CharField(max_length=32)
    telefono = models.CharField(max_length=20, blank=True)

class Rugby(models.Model):
    apellido = models.CharField(max_length=256)
    nombre = models.CharField(max_length=256)
    email = models.EmailField(blank=True)
    dni = models.CharField(max_length=32)
    

class Tenis(models.Model):
    apellido = models.CharField(max_length=256)
    nombre = models.CharField(max_length=256)
    email = models.EmailField(blank=True)
    dni = models.CharField(max_length=32)
    telefono = models.CharField(max_length=20, blank=True)

