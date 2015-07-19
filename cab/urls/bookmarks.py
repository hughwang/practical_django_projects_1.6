from django.conf.urls import *
from cab.views import bookmarks

urlpatterns = patterns('',
    url(r'^add/(?P<snippet_id>\d+)/$',
        bookmarks.add_bookmark,
        name='cab_bookmark_add'),

    url(r'^delete/(?P<snippet_id>\d+)/$',
        bookmarks.delete_bookmark,
        name='cab_bookmark_delete'),
    
    url(r'^$',bookmarks.UserBookMarkListView.as_view(), name='cab_user_bookmarks'),
)