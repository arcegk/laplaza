# -*- encoding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractUser
from . import constants
# Create your models here.


class User(AbstractUser):


	direccion = models.CharField(max_length=50 , verbose_name='dirección')
	telefono = models.CharField(max_length=50  , blank=True , verbose_name='teléfono')
	empresa = models.CharField(max_length=50 )
	token = models.CharField(max_length=500 )

	def __str__(self):
		return self.username



class Plato(models.Model):

	nombre = models.CharField(max_length=25)
	precio = models.FloatField()
	tipo = models.CharField(max_length=25 , choices = constants.TYPE)
	seccion = models.CharField(max_length=25 , choices=constants.SECTION )

	
	def __str__(self):

		return ("%s - %s") %(self.nombre , self.tipo)



class Pedido(models.Model):

	user = models.ForeignKey(User)
	orden = models.ManyToManyField(Plato)
	telefono = models.CharField(max_length=10)
	direccion = models.CharField(max_length=25 )
	empresa = models.CharField(max_length=25 )
	fecha = models.DateTimeField(auto_now_add=True)
	precio = models.FloatField()
	observaciones = models.TextField()
	nombre = models.CharField(max_length=25)



class Menu(models.Model):

	platos = models.ManyToManyField(Plato)

