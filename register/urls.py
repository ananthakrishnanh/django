
from django.conf.urls import include, url
from django.contrib import admin
from register import views
from register.views import *
from register.models import *
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', UserRegistrationView.as_view(), name='register_user'),
    url(r'^user/success/', TemplateView.as_view(template_name='sucess.html'),
        name='page')

]
