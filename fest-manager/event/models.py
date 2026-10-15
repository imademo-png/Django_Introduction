from django.db import models
from django.utils import timezone
from festivals.models import Festival

class Event(models.Model):
    festival = models.ForeignKey(Festival, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    festival = models.ForeignKey(Festival, on_delete=models.CASCADE,related_name='events')
        
    def __str__(self):
        return self.name

    def status(self):
            now = timezone.now()
            if now < self.start_time:
                return "Prochainement !"
            if now > self.end_time:
                return "Fini !"
            return "En cours !"
