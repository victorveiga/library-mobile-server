from django.db import models
from customer.models import Customer
from book.models import Book

# Create your models here.
class Movement(models.Model):
    status   = models.IntegerField(choices=[(1, 'Loan'),(2, 'Return')], default=1)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, unique=False)
    date     = models.DateField()
    books    = models.ManyToManyField(Book, verbose_name='book_movement', related_name="book_movement_set", related_query_name="book")
    loan_id  = models.IntegerField(null=True, blank=True)