from django.shortcuts import render
from django.http import HttpResponseRedirect , Http404
from django.urls import reverse
from .models import Food , Workout
from .forms import FoodForm , WorkoutForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    """The home page for calorie counter"""
    return render(request, 'calorie_counter_app/index.html')

@login_required
def myInfo(request):
    #SHOW ALL FOODS THAT USER ENTERED 
    foods = Food.objects.filter(owner= request.user).order_by('date_added')
    workouts = Workout.objects.filter(owner = request.user).order_by('date_added')
    caloriesEating = 0
    calorieBurned = 0
    for food in foods:
        caloriesEating = caloriesEating + food.calories
    for workout in workouts:
        calorieBurned = calorieBurned + workout.calories_burned
    final_calorie = caloriesEating - calorieBurned
    context = {'foods' : foods , 'workouts' : workouts , 'calorieEating' : caloriesEating , 'calorieBurned' : calorieBurned , 'final_calorie' : final_calorie}
    return render(request , 'calorie_counter_app/myInfo.html' , context)

@login_required
def food(request , food_id):
    food = Food.objects.get(id = food_id)
    if food.owner != request.user:
        raise Http404
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

@login_required
def new_food(request):
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = FoodForm()
    else:
        # POST data submitted; process data.
        form = FoodForm(request.POST)
        if form.is_valid():
            new_food = form.save(commit=False)
            new_food.owner = request.user
            new_food.save()
            return HttpResponseRedirect(reverse('calorie_counter_app:myInfo'))
    context = {'form': form}
    return render(request, 'calorie_counter_app/new_food.html', context)

@login_required
def edit_food(request, food_id):
    """Edit an existing food."""
    food = Food.objects.get(id=food_id)
    if food.owner != request.user:
        raise Http404
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

@login_required
def delete_food(request , food_id):
    """Delete a existing food."""
    food = Food.objects.get(id=food_id)
    if food.owner != request.user:
        raise Http404
    food.delete()
    return HttpResponseRedirect(reverse('calorie_counter_app:myInfo'))

@login_required
def workout(request , workout_id):
    workout = Workout.objects.get(id = workout_id)
    if workout.owner != request.user:
        raise Http404
    name = workout.name
    time = workout.time
    calories_burned = workout.calories_burned
    context = {'workout' : workout , 'name' : name , 'time' : time , 'calories_burned' : calories_burned}
    return render(request , 'calorie_counter_app/workout.html' , context)

@login_required
def new_workout(request):
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = WorkoutForm()
    else:
        # POST data submitted; process data.
        form = WorkoutForm(request.POST)
        if form.is_valid():
            new_workout = form.save(commit=False)
            new_workout.owner = request.user
            new_workout.save()
            return HttpResponseRedirect(reverse('calorie_counter_app:myInfo'))
    context = {'form': form}
    return render(request, 'calorie_counter_app/new_workout.html', context)

@login_required
def edit_workout(request, workout_id):
    """Edit an existing workout."""
    workout = Workout.objects.get(id=workout_id)
    if workout.owner != request.user:
        raise Http404
    if request.method != 'POST':
        # Initial request; pre-fill form with the current food.
        form = WorkoutForm(instance=workout)
    else:
        # POST data submitted; process data.
        form = WorkoutForm(instance=workout, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('calorie_counter_app:workout', args=[workout.id]))
    context = {'workout' : workout, 'form': form}
    return render(request, 'calorie_counter_app/edit_workout.html', context)

@login_required
def delete_workout(request , workout_id):
    """Delete a existing workout."""
    workout = Workout.objects.get(id=workout_id)
    if workout.owner != request.user:
        raise Http404
    workout.delete()
    return HttpResponseRedirect(reverse('calorie_counter_app:myInfo'))