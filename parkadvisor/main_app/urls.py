from django.urls import path 
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('parks/', views.parks_index, name ='index'),
    path('about/', views.about, name='about'),
]