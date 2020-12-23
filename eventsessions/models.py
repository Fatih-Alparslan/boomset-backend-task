from django.db import models

from events.models import Event

class EventSession(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    start_date = models.DateField()
    end_date = models.DateField()
    speaker = models.CharField(max_length=128)



