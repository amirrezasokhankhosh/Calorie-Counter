from django.shortcuts import render
from .models import Food

# Create your views here.
def index(request):
    """The home page for calorie counter"""
    return render(request, 'calorie_counter_app/index.html')

def foods(request):
    #SHOW ALL FOODS THAT USER ENTERED 
    foods = Food.objects.order_by('date_added')
    calories = 0
    for food in foods:
        calories = calories + food.calories
    context = {'foods' : foods , 'calories' : calories}
    return render(request , 'calorie_counter_app/foods.html' , context)

def food(request , food_id):
    food = Food.objects.get(id = food_id)
    name = food.name
    calories = food.calories
    carbohydrates = food.carbohydrates
    cholestrol = food.cholestrol
    fat = food.fat
    fiber = food.fiber
    protein = food.protein
    saturated_fat = food.saturated_fat
    context = {'food' : food , 'name' : name , 'calories' : calories , 'carbohydrates' : carbohydrates , 'fat' : fat , 'fiber' : fiber , 'protein' : protein , 'saturated_fat' : saturated_fat}
    return render(request , 'calorie_counter_app/food.html' , context)

