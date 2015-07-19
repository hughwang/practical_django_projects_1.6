from django.conf.urls import patterns, include, url
from coltrane.models import Category
from coltrane.views import CategoryDetailView
from django.conf import settings
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.dates import DateDetailView, YearArchiveView, MonthArchiveView, DayArchiveView

urlpatterns = patterns('',
    url(r'^$', ListView.as_view(model=Category), name='coltrane_category_list'),
    url(r'^(?P<slug>[-\w]+)/{0,1}$', CategoryDetailView.as_view(), name="coltrane_category_detail"),
)


