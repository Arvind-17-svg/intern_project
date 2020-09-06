from django.urls import path
from . import views
urlpatterns = [
    path('',views.Home,name='Home'),
    path('display',views.Display,name='display'),
     path('medicine_match/',views.medicine_match,name='medicine_match'),
     path('Ingrid_match/',views.Ingrid_match,name='Ingredients_match'),
     path('Home/',views.Home,name='Home'),
]
