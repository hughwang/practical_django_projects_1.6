from django.conf.urls import patterns, include, url
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.dates import DateDetailView, YearArchiveView, MonthArchiveView, DayArchiveView
#from tagging.views import TaggedObjectList

from coltrane.models import Entry, Link

from tagging.models import Tag




#urlpatterns = patterns('',
#    url(r'^widgets/tag/(?P<tag>[^/]+(?u))/$',
#        TaggedObjectList.as_view(model=Widget, paginate_by=10, allow_empty=True),
#        name='widget_tag_detail'),
#)



urlpatterns = patterns('',
    url(r'^$',
        ListView.as_view(queryset=Tag.objects.all(),
                         template_name='coltrane/tag_list.html'),
                         name='coltrane_tag_list'),
    url(r'^tags/entries/(?P<tag>[-\w]+)/$',
        'tagging.views.tagged_object_list',
	#'TaggedListView.as_view()',
	#TaggedObjectList.as_view( paginate_by=10, allow_empty=True),
        {'queryset_or_model': Entry.live.all(),
         'template_name': 'coltrane/entries_by_tag.html'},
         name='coltrane_entry_archive_tag'),

    url(r'^links/(?P<tag>[-\w]+)/$',
        'tagging.views.tagged_object_list',
        {'queryset_or_model': Link.objects.all(),
         'template_name': 'coltrane/links_by_tag.html'},
         name='coltrane_link_archive_tag'),

)
