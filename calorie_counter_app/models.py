from django.db import models

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
    def __str__(self):
        """Return a string representation of the model."""
        return self.name
