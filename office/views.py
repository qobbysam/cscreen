from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.


class OfficeHomeView(TemplateView):
    template_name = 'office/officehome.html'

