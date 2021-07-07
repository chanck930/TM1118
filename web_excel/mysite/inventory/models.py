from django.db import models

# Create your models here.
class Entry(models.Model):
    #Fields
    inventory = models.CharField(max_length=10)
    loc = models.CharField(max_length=10)
    endUser = models.CharField(max_length=50)
    description = models.TextField()
    brand = models.CharField(max_length=10,blank=True, null=True)
    unitPrice = models.IntegerField()
    acqDate = models.DateTimeField()
    
    class Meta:
        verbose_name_plural = 'entries'

    #Methods
    def __str__(self):
        return self.inventory