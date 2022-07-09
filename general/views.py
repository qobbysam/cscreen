from django.shortcuts import render

from django.views.generic.base import TemplateView
from django.contrib.auth import views as auth_views
from django.shortcuts import resolve_url
from general import forms
# Create your views here.


class HomepageView(TemplateView):
    template_name = 'general/home.html'

def registerView(request):
    if request.method == 'GET':
        form  = forms.RegisterForm()
        context = {'form': form}
        return render(request, 'general/register.html', context)


class LoginView(auth_views.LoginView):
    template_name = 'general/login.html'

    def get_success_url(self):
        return resolve_url('clientHome')




    
def logoutView(request):
    pass


