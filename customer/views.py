from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Customer
from .serializers import CustomerSerializer

# Create your views here.
class CustomerViewSet(ModelViewSet):
    serializer_class = CustomerSerializer

    def get_queryset(self):
        return Customer.objects.all()