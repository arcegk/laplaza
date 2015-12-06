# -*- encoding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractUser
from . import constants
# Create your models here.


class User(AbstractUser):

	empresa = models.CharField(max_length=50 )
	token = models.CharField(max_length=500 )

	def __unicode__(self):
		return self.username



class Plato(models.Model):

	nombre = models.CharField(max_length=100)
	precio = models.FloatField()
	tipo = models.CharField(max_length=25 , choices = constants.TYPE)
	seccion = models.CharField(max_length=25 , choices=constants.SECTION )
	precio_extra = models.FloatField(default= 0)

	
	def __unicode__(self):

		return ("%s - %s") %(self.nombre , self.tipo)



class Pedido(models.Model):

	user = models.ForeignKey(User)
	orden = models.ManyToManyField(Plato)
	telefono = models.CharField(max_length=10)
	direccion = models.CharField(max_length=50 )
	empresa = models.CharField(max_length=25 )
	fecha = models.DateTimeField(auto_now_add=True)
	precio = models.FloatField()
	observaciones = models.TextField(blank=True)
	nombre = models.CharField(max_length=25)
	estado = models.CharField(max_length=25)



class Menu(models.Model):

	platos = models.ManyToManyField(Plato)


class Config(models.Model):

	telefono = models.CharField(max_length=10)


class Ubicacion(models.Model):

	lat = models.CharField(max_length=200)
	lon = models.CharField(max_length=200)
	fecha = models.DateField(auto_now_add=True)


