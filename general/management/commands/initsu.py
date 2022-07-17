import os
from django.conf import settings
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):

        username = os.environ.get('DJANGO_ADMIN_USERNAME')
        password = os.environ.get('DJANGO_ADMIN_PASSWORD')

        try:
            su = User.objects.create_superuser(username=username, password=password)

            su.save()
            print("created account %s ", username)
        
        except:

            print("user already existed,  ", username)

            

        
