from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from eventsessions.models import EventSession


class EventSessionSerializer(ModelSerializer):
    class Meta:
        model = EventSession
        fields = '__all__'

    def validate(self, value):
        if value['start_date'] > value['end_date']:
            raise serializers.ValidationError({"end_date": "End date must be after than start date"})
        return value

