from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Book
from .serializers import BookSerializer

# Create your views here.
class BookViewSet(ModelViewSet):
    serializer_class = BookSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes     = [IsAuthenticated]

    def get_queryset(self):
        queryset = Book.objects.all()
        queryset = queryset.order_by('-id')
        return queryset