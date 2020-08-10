from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#FOOD MODEL
class Food(models.Model):
    name = models.CharField(max_length=200)
    calories = models.PositiveIntegerField()
    carbohydrates = models.PositiveIntegerField()
    cholestrol = models.PositiveIntegerField()
    fat = models.PositiveIntegerField()
    fiber = models.PositiveIntegerField()
    protein = models.PositiveIntegerField()
    saturated_fat = models.PositiveIntegerField()
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User , on_delete = models.CASCADE)

    def __str__(self):
        """Return a string representation of the model."""
        return self.name

class Workout(models.Model):
    name = models.CharField(max_length=200)
    time = models.PositiveIntegerField()
    calories_burned = models.PositiveIntegerField()
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User , on_delete = models.CASCADE)

    def __str__(self):
        return self.name
    

