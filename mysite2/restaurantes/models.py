from django.db import models

class Restaurate(models.Model):
	nombre = models.CharField(max_length=100)
	ubicacion = models.CharField(max_length=100)
	telefono = models.CharField(max_length=8)
	def __str__(self):
		return self.nombre

