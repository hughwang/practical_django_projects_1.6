from django.conf.urls import patterns, url

#from django.views.generic.list_detail import object_list
from django.views.generic.list import ListView

from cab.models import Language
from cab.views.languages import SubListView

language_info = { 'queryset': Language.objects.all(),
                  'paginate_by': 20 }

urlpatterns = patterns('',
    url(r'^$',
        ListView.as_view(queryset=Language.objects.all(),
                         paginate_by=20),
                         name='cab_language_list'),
    url(r'^(?P<slug>[-\w]+)/$',
        SubListView.as_view(),
        name='cab_language_detail'),
)

