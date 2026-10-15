from django.db import models

class Festival(models.Model):
    name = models.CharField(max_length=64)
    location = models.CharField(max_length=64)
    capacity = models.PositiveSmallIntegerField()
    start_date = models.DateField()
    end_date = models.DateField()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
    
    