from django.urls import path
from office import views
urlpatterns = [
    path('', views.OfficeHomeView.as_view(), name="officeHome" ),
    
]
