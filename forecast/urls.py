from django.urls import path
from . import views

urlpatterns = [
    path('', views.weather_view, name='weather_view'),
    path('api/city_search_counts/', views.city_search_count_view, name='city_search_counts'),
]