from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include

from general import views
urlpatterns = [
    path('', views.HomepageView.as_view(), name="genHome" ),
    path('register/', views.registerView, name="genRegister"),
    path('login/', views.loginview, name="genLogin"),
    path('logout/', views.logoutView, name="genLogout"),
    path('susu/', include('susu.urls')),
    path('client/', include('client.urls')),
    path('office/', include('office.urls'))


]