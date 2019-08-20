from django.db import models

class Plant(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    purchased_date = models.DateField(blank=True,null=True)
