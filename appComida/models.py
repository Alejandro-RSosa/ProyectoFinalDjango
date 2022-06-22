from django.db import models

# Create your models here.

class Perros(models.Model):
    nombre = models.CharField(max_length=20)
    desc = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Nombre: {self.nombre} - Descripcion: {self.desc} - Precio: {self.precio}"

class Gatos(models.Model):
    nombre = models.CharField(max_length=20)
    desc = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Nombre: {self.nombre} - Descripcion: {self.desc} - Precio: {self.precio}"

class Snacks(models.Model):
    nombre = models.CharField(max_length=20)
    desc = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Nombre: {self.nombre} - Descripcion: {self.desc} - Precio: {self.precio}"