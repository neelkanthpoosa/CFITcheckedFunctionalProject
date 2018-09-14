from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.utils import timezone

# Create your models here.
class Post(models.Model):
	post=models.CharField(max_length=500)
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	created=models.DateTimeField(auto_now_add=True)
	updated=models.DateTimeField(auto_now=True)
	image=models.ImageField(upload_to='CBIT_Market_Place/media/post_image',blank=True)

    # def __str__(self):
    #     return self.user.username



class Item(models.Model):
	CHOICES=(
	('Drafter','Drafter'),
	('Apron','Apron'),
    ('Calculator','Calculator'),
    ('Power Bank','Power Bank'),
    ('Book','Book'),
	)
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	item = models.CharField(max_length=255,choices=CHOICES)
	created_date=models.DateTimeField(default=timezone.now)

	class Meta:
		verbose_name = 'Item'
		verbose_name_plural = 'Item'



class SellerStatus(models.Model):
	CHOICES=(
	('Available','Available'),
	('Not Available','Not Available'),
	)
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	status = models.CharField(max_length=255,choices=CHOICES)
	created_date=models.DateTimeField(default=timezone.now)

	class Meta:
		verbose_name = 'Status'
		verbose_name_plural = 'Status'
