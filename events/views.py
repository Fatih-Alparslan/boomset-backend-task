from rest_framework.viewsets import ModelViewSet

from boom.utils import StandardResultsSetPagination
from events.models import Event
from events.serializers import EventSerializer


class EventViewSet(ModelViewSet):
    model = Event
    serializer_class = EventSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        return Event.objects.all()