from django.conf.urls import url
from . import views

urlpatterns = [
    # Home page
    url(r'^$', views.index, name='index'),

    #SHOW ALL FOODS THAT USER ENTERED
    url(r'^foods$' , views.foods , name='foods'),
    url(r'^foods/(?P<food_id>\d+)/$', views.food, name='food'),
]