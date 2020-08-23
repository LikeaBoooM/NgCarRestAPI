from django.db import models

# Create your models here.

class Car(models.Model):
    mark = models.CharField(max_length=180)
    model = models.CharField(max_length=180)