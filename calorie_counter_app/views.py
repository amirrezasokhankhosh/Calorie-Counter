from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Food
from .forms import FoodForm

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

def new_food(request):
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = FoodForm()
    else:
        # POST data submitted; process data.
        form = FoodForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('calorie_counter_app:foods'))
    context = {'form': form}
    return render(request, 'calorie_counter_app/new_food.html', context)

def edit_food(request, food_id):
    """Edit an existing food."""
    food = Food.objects.get(id=food_id)
    if request.method != 'POST':
        # Initial request; pre-fill form with the current food.
        form = FoodForm(instance=food)
    else:
        # POST data submitted; process data.
        form = FoodForm(instance=food, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('calorie_counter_app:food', args=[food.id]))
    context = {'food' : food, 'form': form}
    return render(request, 'calorie_counter_app/edit_food.html', context)
