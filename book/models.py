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
    status      = models.IntegerField(choices=[(1, 'Available'), (2, 'Checked Out'), (3, 'Not Available'), (4, 'On Hold')], default=1)

    def __str__(self):
        return self.title