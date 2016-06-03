from register.views import *
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
url(r'^$', UserRegistrationView.as_view(), name='register_user'),
        ]