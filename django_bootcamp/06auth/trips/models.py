from django.db import models

# get_user_model() returns the active User model in the project.
from django.contrib.auth import get_user_model

from django.core.validators import MaxValueValidator

User = get_user_model()

# Create your models here.
class Trip(models.Model):
    city = models.CharField(max_length=15)
    country = models.CharField(max_length=2)  # 2CHAR code
    #start_date = models.DateField(blank=True, null=True)
    #end_date = models.DateField(blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='trips')

    def __str__(self):
        return self.city


class Note(models.Model):
    TRIP_TYPES = (
        ('event', 'Event'),
        ('retreat', 'Retreat'),
        ('family', 'Family'),
    )
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='notes')
    title = models.CharField(max_length=100)
    description = models.TextField()
    type = models.CharField(max_length=10, choices=TRIP_TYPES)
    rating = models.PositiveSmallIntegerField(default=1, validators=[MaxValueValidator(5)])
    img = models.ImageField(upload_to='notes', blank=True, null=True)

    def __str__(self):
        return f'{self.title} in {self.trip.city}'
