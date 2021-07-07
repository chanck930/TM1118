from django.db import models

# Create your models here.
class Event(models.Model):
    #Fields
    node_id = models.CharField(max_length=2)
    node_loc = models.CharField(max_length=10)
    temp = models.DecimalField(max_digits=5, decimal_places=2)
    date_created = models.DateTimeField(auto_now_add=True)
    
    #Methods
    def __str__(self):
        return 'Event #{}'.format(self.id)

class VenueEvent(models.Model):
    venue = models.CharField(max_length=10)
    date = models.DateField()
    timeStart = models.TimeField()
    timeEnd = models.TimeField()
    event = models.CharField(max_length=10)
    instructor = models.CharField(max_length=50)

    #Methods
    def __str__(self):
        return f'{self.venue} @ {self.date}'