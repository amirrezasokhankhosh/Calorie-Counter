from django.conf.urls import url
from . import views

urlpatterns = [
    # Home page
    url(r'^$', views.index, name='index'),

    #SHOW ALL FOODS THAT USER ENTERED
    url(r'^myInfo/$' , views.myInfo , name='myInfo'),
    url(r'^myInfo/foods/(?P<food_id>\d+)/$', views.food, name='food'),
    url(r'^new_food/$', views.new_food, name='new_food'),
    url(r'^edit_food/(?P<food_id>\d+)/$', views.edit_food,name='edit_food'),
    url(r'^delete_food/(?P<food_id>\d+)/$' , views.delete_food , name='delete_food'),
    url(r'^myInfo/workout/(?P<workout_id>\d+)/$' , views.workout , name='workout'),
    url(r'^new_workout/$' , views.new_workout , name='new_workout'),
    url(r'^edit_workout/(?P<workout_id>\d+)/$', views.edit_workout,name='edit_workout'),
    url(r'^delete_workout/(?P<workout_id>\d+)/$' , views.delete_workout , name='delete_workout'),
]