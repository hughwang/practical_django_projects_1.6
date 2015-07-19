from django.conf.urls import *
from cab.views.home import home

urlpatterns = patterns('',
    url(r'^$', home, name='cab_home'),
)
