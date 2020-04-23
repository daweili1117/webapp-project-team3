from django.db import models
from django.contrib.auth.models import User



class Reservation(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    num = models.CharField(max_length=255, blank=True)
    date = models.DateField()
    time = models.TimeField()
    guests = models.SmallIntegerField()
    requests = models.TextField()


    def __str__(self):
        return self.name
