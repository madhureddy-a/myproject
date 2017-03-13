from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Publication(models.Model):
	pub = models.CharField(max_length=100)
		
	def __unicode__(self):
		return self.pub


class Book(models.Model):
	book = models.CharField(max_length=100)
	pub_id = models.OneToOneField(Publication)
	
	def __unicode__(self):
		return self.book


class Publication_MM(models.Model):
	pub = models.CharField(max_length=100)

	def __unicode__(self):
		return self.pub

class Book_MM(models.Model):
	book = models.CharField(max_length=100)
	pub_id = models.ManyToManyField(Publication_MM)
	
	def __unicode__(self):
		return self.book

class signup(models.Model):
	fname=models.CharField(max_length=100)
	lname=models.CharField(max_length=50)
	age=models.IntegerField()
	address=models.CharField(max_length=100)
	mobileno=models.IntegerField()

	def __unicode__(self):
		return self.fname