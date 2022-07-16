from django.shortcuts import render

from django.views.generic.base import TemplateView
from django.contrib.auth import views as auth_views
from django.shortcuts import resolve_url
from django.contrib.auth.forms import AuthenticationForm #add this
from django.contrib.auth import login, authenticate #add this
from django.contrib import messages


from general import forms
# Create your views here.


class HomepageView(TemplateView):
    template_name = 'general/home.html'

def registerView(request):
    if request.method == 'GET':
        form  = forms.RegisterForm()
        context = {'form': form}
        return render(request, 'general/register.html', context)

    if request.method == 'POST':
        form = forms.RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()

            context = {'message': "added success"}


            return render(request, 'general/register.html', context)
        else:
           # msg = " added not success %s" % 
            context = {'form':form}


            return render(request, 'general/register.html', context)



def loginview(request):
    # if request.method = 'Get'
    #     form  = forms.RegisterForm()
    #         context = {'form': form}
    #         return render(request, 'general/register.html', context)
    
    if request.method == 'Post':

        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                if user.groups.filter(name='client').exists():

                    return resolve_url('clientHome')
                elif user.groups.filter(name='office'):

                    return resolve_url('officeHome')
                elif user.groups.filter(name='susu'):
                    return resolve_url('susuHome')
                
                else:
                    return resolve_url('unauthorized')
                
            else:
                messages.error(request,"Invalid username or password.")
    else:
        messages.error(request,"Invalid username or password.")
        form = AuthenticationForm()
        return render(request=request, template_name="general/login.html", context={"login_form":form})


# class LoginView(auth_views.LoginView):
#     template_name = 'general/login.html'

#     def get_success_url(self):

#         if self.user.groups.filter(name='client').exists():

#             return resolve_url('clientHome')
#         elif self.user.groups.filter(name='office'):

#             return resolve_url('officeHome')
#         elif self.user.groups.filter(name='susu'):
#             return resolve_url('susuHome')
        
#         else:
#             return resolve_url('unauthorized')




    
def logoutView(request):
    pass


