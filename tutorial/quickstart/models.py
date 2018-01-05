# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Champion(models.Model):
	name = models.CharField(max_length=45)
	skills = models.CharField(max_length=45)
	story = models.CharField(max_length=45)
	
	def __str__(self):
		return self.name

class Item(models.Model):
	name = models.CharField(max_length=45)
	price = models.CharField(max_length=45)
	passive = models.CharField(max_length=45)
	
	def __str__(self):
		return self.name