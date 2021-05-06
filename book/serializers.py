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
        return 1
        queryset        = Movement.objects.all()
        queryset_load   = queryset.filter(status__iexact=1)
        queryset_load   = queryset_load.filter(books__in=[instance.id])
        queryset_return = queryset.filter(status__iexact=2)
        queryset_return = queryset_return.filter(books__in=[instance.id])
        
        if (len(queryset_load) > len(queryset_return)):
            return 2 # Not Available | Chacked out
        else:
            return 1