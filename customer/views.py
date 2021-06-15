from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Customer
from .serializers import CustomerSerializer

# Create your views here.
class CustomerViewSet(ModelViewSet):
    serializer_class       = CustomerSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes     = [IsAuthenticated]

    def get_queryset(self):
        return Customer.objects.all()