# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.contrib.gis.db import models

from django.contrib.contenttypes.models import ContentType

class Event(models.Model):
	name = models.CharField(max_length=64, verbose_name='nombre')
	description = models.TextField(blank=True, null=True, verbose_name='descripción')
	front_image = models.ImageField(
		upload_to='showcase/events/', 
		null=True, blank=True, 
		verbose_name = 'portada'
	)	 	
	latitude = models.FloatField()
	longitude = models.FloatField(default=0)
	start = models.DateTimeField()
	ends = models.DateTimeField(blank=True, null=True)	
	cover = models.DecimalField(
		decimal_places=2, max_digits=8, 
		blank=True, null=True,
		verbose_name = 'precio de entrada'
	)
	is_public = models.BooleanField(default=False)
	link = models.CharField(max_length=128, blank=True, null=True)
	date_joined = models.DateTimeField(auto_now_add=True)		
	guests = models.ManyToManyField(User, through='Guest')

	def __unicode__(self):
		return self.name

	def get_organizer(self):
		organizers = self.guests.filter(guests__is_organizer=True)
				
		if len(organizers) > 0:
			return organizers[0]
		return None


class Guest(models.Model):
	class Meta:
		unique_together = (('user', 'event'),)

	STATE_CHOICES = (
		(1, 'Invitado'),
		(2, 'Asistirá'),
		(3, 'Talvez asista'),
		(4, 'No asistirá')
	)

	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='guests')
	event = models.ForeignKey(Event, on_delete=models.CASCADE)
	is_creator = models.BooleanField(default=False)
	is_organizer = models.BooleanField(default=False)
	state = models.PositiveSmallIntegerField(default = 1, choices = STATE_CHOICES) 
	date = models.DateTimeField(auto_now_add=True)

	def attend(self, action=True):
		self.state = 2 if action else 3		


class Category(models.Model):
	name = models.CharField(max_length=64, unique=True)

	def __unicode__(self):
		return self.name

class Locality(models.Model):
	name = models.CharField(max_length=45, verbose_name='nombre')
	description = models.TextField(blank=True, null=True, verbose_name='descripción')
	front_image = models.ImageField(upload_to='showcase/localities/', blank=True, null=True)
	profile_image = models.ImageField(upload_to='showcase/localities/', blank=True, null=True)	
	latitude = models.FloatField(verbose_name='latitud')
	longitude = models.FloatField(verbose_name='longitud')
	point = models.PointField(null=True, blank=True)
	is_public = models.BooleanField(default=False, verbose_name='visible a todos?')
	verified = models.BooleanField(default=False,)	
	date_joined = models.DateTimeField(auto_now_add=True)	
	owner = models.ForeignKey(User)	
	categories = models.ManyToManyField(Category, verbose_name='categorias')

	def __unicode__(self):
		return self.name

class Commercial(models.Model):
	ruc = models.CharField(max_length=13)
	locality = models.OneToOneField(Locality, on_delete=models.CASCADE)		
	
	def __unicode__(self):
		return self.locality.name

class Group(models.Model):
	KIND_CHOICES = (
		(1, 'Producto'),
		(2, 'Servicio')
	)

	name = models.CharField(max_length=64)
	kind = models.PositiveSmallIntegerField(choices = KIND_CHOICES)
	commercial = models.ForeignKey(Commercial)

	def __unicode__(self):
		return self.name

class Offer(models.Model):
	name = models.CharField(max_length=64)
	price = models.DecimalField(max_digits=10, decimal_places=2, default=0)	
	image = models.ImageField(upload_to='showcase/offers/', null=True, blank=True)
	group = models.ForeignKey(Group)

	def __unicode__(self):
		return unicode(self.name)

class Subscriber(models.Model):
	contenttype = models.ForeignKey(ContentType, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)	