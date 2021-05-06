from rest_framework.serializers import ModelSerializer, ValidationError, SerializerMethodField
from .models import Book
from movement.models import Movement

class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    status = SerializerMethodField()      

    # Custom fields functions #
    def get_status(self, instance):
        queryset        = Movement.objects.all()
        queryset_load   = queryset.filter(status__iexact=1).filter(books__in=[instance.id])
        queryset_return = queryset.filter(status__iexact=2).filter(books__in=[instance.id])
        
        if (len(queryset_load) > len(queryset_return)):
            return 2 # Not Available | Chacked out
        else:
            return 1