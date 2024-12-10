from django.db import models

# Create your models here.

class Componente(models.Model):
    nombre = models.CharField(max_length=40)
    cantidad = models.IntegerField()

    def __str__(self):
        return f"ComponenteNombre: {self.nombre} - Cantidad: {self.cantidad}"

class Colaborador(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    profesion = models.CharField(max_length=30)

    def __str__(self):
        return f"Colaborador: {self.nombre}  {self.apellido} - {self.email} - {self.profesion}"

class Sede(models.Model):
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30)
    nro_tel = models.CharField(max_length=30)

    def __str__(self):
        return f"Sede: {self.nombre} - Dirección: {self.direccion} - nro_tel: {self.nro_tel}"


