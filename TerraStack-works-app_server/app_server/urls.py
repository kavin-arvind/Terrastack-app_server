from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('village-maps/', views.get_village_maps, name='village_maps'),
    path('', views.index, name='index'),
    path('village-maps/geojson', geojson_list, name='village_maps_geojson'),
]