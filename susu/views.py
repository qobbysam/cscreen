from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.


class SusuHomeView(TemplateView):
    template_name = 'susu/susuhome.html'