from django.db import models
from datetime import datetime, timedelta


# Create your models here.
class Reminder(models.Model):
    Name = models.CharField(max_length=255)
    Date = models.DateField(null=True)
    Time = models.TimeField(null=True)
    Description = models.TextField(null=False,blank=False)

