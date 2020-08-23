from django.db import models

# Create your models here.

class Car(models.Model):
    mark = models.CharField(max_length=180)
    model = models.CharField(max_length=180, unique=True)

    def __str__(self):
        return "Car mark : {} Car model {}".format(self.id,self.model)
    

class Rate(models.Model):
    class Ratings(models.IntegerChoices):
        One = 1 
        Two = 2
        Three = 3
        Four = 4
        Five = 5
    
    grade = models.IntegerField(choices=Ratings.choices)
    car = models.ForeignKey(Car, on_delete=models.CASCADE,blank=True, null=True, related_name='rates')
