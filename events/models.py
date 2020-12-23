from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=128)
    start_date = models.DateField()
    end_date = models.DateField()
    timezone = models.CharField(max_length=128)

    def __str__(self):
        return self.name

