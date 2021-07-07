from django.db import models

# Create your models here.
class Entry(models.Model):
    #Fields
    text = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'entries'

    #Methods
    def __str__(self):
        return 'Entry #{}'.format(self.id)