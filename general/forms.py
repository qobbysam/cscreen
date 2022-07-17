from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.core.exceptions import ValidationError
class RegisterForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField()
    password2 = forms.CharField()
    account = forms.CharField()

    def clean(self):
        c_data = super().clean()

        pass1 = c_data.get("password1")
        pass2 = c_data.get("password2")

        if pass1 != pass2:

            raise ValidationError("passwords are not equal")


    def save(self, commit=True):
        new_create , user = User.objects.get_or_create(
            username = self.cleaned_data['email'],
            password = self.cleaned_data['password1'],
        )

        if user:
            if commit:
                

                    new_create.save()
                    group = Group.objects.get(name=self.cleaned_data['account'])
                    group.user_set.add(new_create)

                    return new_create
        else:
            print("duplicate item")

            

        return new_create

