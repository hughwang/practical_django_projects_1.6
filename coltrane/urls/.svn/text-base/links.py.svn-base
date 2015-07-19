from django.conf.urls import patterns, include, url
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.dates import  ArchiveIndexView, DateDetailView, YearArchiveView, MonthArchiveView, DayArchiveView

from coltrane.models import Link



urlpatterns = patterns(  'django.views.generic.dates',  
    url(r'^$',ArchiveIndexView.as_view(queryset=Link.objects.all(), date_field='pub_date'), name='coltrane_link_archive_index'),
    url(r'^(?P<year>\d{4})/{0,1}$', YearArchiveView.as_view(model=Link, date_field="pub_date", make_object_list = True), name='coltrane_link_archive_year'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/{0,1}$', MonthArchiveView.as_view(model=Link, date_field="pub_date", month_format="%m"), name='coltrane_link_archive_month'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/{0,1}$', DayArchiveView.as_view(model=Link, date_field="pub_date", month_format="%m"), name='coltrane_link_archive_day'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[-\w]+)/{0,1}$', DateDetailView.as_view(model=Link, date_field="pub_date", month_format="%m"), name='coltrane_link_detail'),
)