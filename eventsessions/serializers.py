from rest_framework.serializers import ModelSerializer

from eventsessions.models import EventSession


class EventSessionSerializer(ModelSerializer):
    class Meta:
        model = EventSession
        fields = '__all__'