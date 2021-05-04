from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Book
from .serializers import BookSerializer

# Create your views here.
class BookViewSet(ModelViewSet):
    serializer_class = BookSerializer

    def get_queryset(self):
        return Book.objects.all()