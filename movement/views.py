from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .models import Movement
from .serializers import MovementSerializer
from rest_framework.decorators import action
from rest_framework import status
from django.shortcuts import get_object_or_404
from movement.models import Movement
from book.models import Book
from .utils import get_closed_movement
import datetime

# Create your views here.
class MovementViewSet(ModelViewSet):
    serializer_class = MovementSerializer

    def get_queryset(self):
        status = self.request.query_params.get('status', None)

        queryset = Movement.objects.all() 

        if status:
            queryset = queryset.filter(status=status)

        return queryset
    
    def destroy(self, request, *args, **kwargs):
        return Response(data={'message': 'Request not allowed'}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        return Response(data={'message': 'Request not allowed'}, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, *args, **kwargs):
        return Response(data={'message': 'Request not allowed'}, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['post'], detail=False)
    def make_return(self, request):
        loan_param  = request.data.get('loan', None)
        books_param = request.data.get('books', None)

        if not loan_param:
            return Response(data={'message': 'The loan identification is required.'}, status=status.HTTP_400_BAD_REQUEST)

        if not books_param:
            return Response(data={'message': 'The books identification is required.'}, status=status.HTTP_400_BAD_REQUEST)

        loan_movement            = get_object_or_404(Movement, pk=loan_param)        
        if loan_movement.status == 2:
            return Response(data={'message': 'It´s not possible to make a book return from a return.'}, status=status.HTTP_400_BAD_REQUEST)

        if get_closed_movement(loan_movement) == True:
            return Response(data={'message': 'It´s not possible to make a book return from a closed loan.'}, status=status.HTTP_400_BAD_REQUEST)

        return_movement          = Movement()
        return_movement.customer = loan_movement.customer
        return_movement.date     = datetime.date.today()
        return_movement.status   = 2
        return_movement.loan_id  = loan_movement.id
        return_movement.save()
        for book_id in books_param:
            return_movement.books.add(loan_movement.books.get(id=book_id))
            
        return_movement.save()
            
        return Response(data={'message': 'Successful'})