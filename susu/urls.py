
from django.urls import path, include
from susu import views
urlpatterns = [
    path('', views.susuHomeView, name="susuHome"),
    
]
