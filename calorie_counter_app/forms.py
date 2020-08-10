from django import forms
from .models import Food , Workout

class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ['name' , 'calories' , 'carbohydrates' , 'cholestrol' , 'fat' , 'fiber' , 'protein' , 'saturated_fat']

class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['name' , 'time' , 'calories_burned']