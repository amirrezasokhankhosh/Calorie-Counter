from django.conf.urls import url
from . import views

urlpatterns = [
    # Home page
    url(r'^$', views.index, name='index'),

    #SHOW ALL FOODS THAT USER ENTERED
    url(r'^foods/$' , views.foods , name='foods'),
    url(r'^foods/(?P<food_id>\d+)/$', views.food, name='food'),
    url(r'^new_food/$', views.new_food, name='new_food'),
    url(r'^edit_food/(?P<food_id>\d+)/$', views.edit_food,name='edit_food'),
    url(r'^delete_food/(?P<food_id>\d+)/$' , views.delete_food , name='delete_food')
]