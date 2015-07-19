from django.conf.urls import *
from cab.views import popular

urlpatterns = patterns('',
    url(r'^authors/$',
        popular.TopAuthorListView.as_view(),
        name='cab_top_authors'),
        
    url(r'^languages/$',
        popular.TopLanguageListView.as_view(),
        name='cab_top_languages'),
    
    url(r'^bookmarks/$', popular.MostBookMarkedListView.as_view(), name='cab_most_bookmarked'),
    
    url(r'^ratings/$', popular.TopRatedListView.as_view(), name='cab_top_rated'),
    
)