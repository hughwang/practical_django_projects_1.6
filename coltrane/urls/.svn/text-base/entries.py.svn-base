from django.conf.urls import patterns, include, url
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.dates import ArchiveIndexView,DateDetailView, YearArchiveView, MonthArchiveView, DayArchiveView

from coltrane.models import Entry

urlpatterns = patterns('django.views.generic.dates',
    #url(r'^/{0,1}$', 'coltrane.views.entries_index'),
    url(r'^$',
        ArchiveIndexView.as_view(queryset=Entry.live.all(),
                                 date_field='pub_date'),
                                 name='coltrane_entry_archive_index'),
   
    url(r'^(?P<year>\d{4})/$',
        YearArchiveView.as_view(queryset=Entry.live.all(),
                                date_field='pub_date'),
                                name='coltrane_entry_archive_year'),

    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/{0,1}$',
        MonthArchiveView.as_view(queryset=Entry.live.all(),
                                 date_field='pub_date'),
                                 name='coltrane_entry_archive_month'),
    

    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/$',
        DayArchiveView.as_view(queryset=Entry.live.all(),
                               date_field='pub_date'),
                               name='coltrane_entry_archive_day'),

    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$',
        DateDetailView.as_view(queryset=Entry.live.all(),
                               date_field='pub_date'),
                               name='coltrane_entry_detail'),


)
