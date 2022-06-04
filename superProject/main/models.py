from django.db import models


class Droid(models.Model):
    name = models.CharField(max_length=20)
    master = models.CharField(max_length=20)
    planet = models.CharField(max_length=30)
    image = models.ImageField(null=True, blank=True,upload_to='images')


class User(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    age = models.CharField(max_length=10)
    city = models.CharField(max_length=20)
    # sex =

class Auto(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    master = models.CharField(max_length=20)
    color = models.CharField(max_length=20)



# Create your models here.
