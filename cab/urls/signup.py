from django.conf.urls import patterns, url
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from django.contrib.auth.models import User
from cab.views.signup import signup


urlpatterns = patterns('',
    url(r'^add/$',
        signup,
        name='cab_signup_add'),
)
