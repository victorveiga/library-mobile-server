from django.db import models

# Create your models here.
class Customer(models.Model):
    firstname = models.CharField(max_length=30)
    lastname  = models.CharField(max_length=50)
    number    = models.CharField(max_length=100)
    email     = models.CharField(max_length=100)