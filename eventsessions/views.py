from rest_framework.viewsets import ModelViewSet

from boom.utils import StandardResultsSetPagination
from eventsessions.models import EventSession
from eventsessions.serializers import EventSessionSerializer


class EventSessionViewSet(ModelViewSet):
    model = EventSession
    serializer_class = EventSessionSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        return EventSession.objects.all()
