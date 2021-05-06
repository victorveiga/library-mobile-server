from rest_framework.serializers import ModelSerializer, ValidationError, SerializerMethodField
from .models import Movement
from .utils import get_closed_movement

class MovementSerializer(ModelSerializer):
    class Meta:
        model = Movement
        fields = '__all__'

    closed = SerializerMethodField()

    def get_closed(self, instance):
        return get_closed_movement(instance)