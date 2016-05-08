# -*- encoding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.crypto import get_random_string
from . import constants
# Create your models here.


class User(AbstractUser):

	empresa = models.CharField(max_length=50 )
	cod_referido = models.CharField(max_length=6, null=True, unique=True)
	padrino  = models.ForeignKey('self', null=True)
	token = models.CharField(max_length=500 )
	is_premium = models.BooleanField(default=False)
	telefono = models.CharField(max_length=10)


	def __unicode__(self):
		return self.username

	def save(self, *args, **kwargs):
		if not self.id:
			c = 'abcdefghijklmnopqrstuvwxyz0123456789'
			self.cod_referido = get_random_string(6,c)
		super(User,self).save(*args,**kwargs)




class Plato(models.Model):

	nombre = models.CharField(max_length=100)
	precio = models.FloatField()
	tipo = models.CharField(max_length=25 , choices = constants.TYPE)
	seccion = models.CharField(max_length=25 , choices=constants.SECTION )
	precio_extra = models.FloatField(default= 0)

	
	def __unicode__(self):

		return ("%s - %s") %(self.nombre , self.tipo)

	def save(self, *args , **kwargs):
		self.nombre = self.nombre.upper()
		super(Plato, self).save(*args, **kwargs)



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

	def __unicode__(self):

		return ("%s , %s") %(self.lat , self.lon)
