from django.db import models

# Create your models here.
class Book(models.Model):
    title       = models.CharField(max_length=50)
    subtitle    = models.CharField(max_length=100)
    author      = models.CharField(max_length=200)
    publisher   = models.CharField(max_length=200)
    isbn        = models.CharField(max_length=255)
    description = models.TextField()
    photo       = models.ImageField(upload_to='books_photos', null=True, blank=True)

    def __str__(self):
        return self.title