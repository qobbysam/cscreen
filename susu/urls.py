
from django.urls import path, include
from susu import views
urlpatterns = [
    path('', views.SusuHomeView.as_view(), name="susuHome"),
    
]
