from django.db import models

# Create your models here.

class Csvfile(models.Model):
    file=models.FileField( upload_to='media', max_length=1000)

class Check(models.Model):
    name=models.CharField(max_length=1000000)