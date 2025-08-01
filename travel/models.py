
from django.db import models

class Destination(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    description = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)

class Booking(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    date = models.DateField()
