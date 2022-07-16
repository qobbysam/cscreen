from django.contrib import admin
from django.urls import path, include

from client import views

urlpatterns = [
    path('', views.ClientHomeView.as_view(), name="clientHome"),
    
]
