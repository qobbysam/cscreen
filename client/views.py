from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.


class ClientHomeView(TemplateView):
    template_name = 'client/clienthome.html'

