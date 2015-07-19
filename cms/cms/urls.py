import os
from django.conf.urls import patterns, include, url
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.dates import DateDetailView, YearArchiveView, MonthArchiveView, DayArchiveView
from django.conf import settings

from coltrane.views import CategoryDetailView
from coltrane.feeds import CategoryFeed, LatestEntriesFeed




from django.contrib import admin
from django.contrib.flatpages import urls
from coltrane.models import Entry,Link

import settings


admin.autodiscover()

feeds = {'entries': LatestEntriesFeed,
         'categories': CategoryFeed}


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cms.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT }),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^tinymce/', include('tinymce.urls')),
    #url(r'^tiny_mce/', include('tinymce.urls')),
    url(r'^weblog/categories/', include('coltrane.urls.categories')),
    url(r'^weblog/links/', include('coltrane.urls.links')),
    url(r'^weblog/tags/', include('coltrane.urls.tags')),
    url(r'^comments/', include('django.contrib.comments.urls')),

    url(r'^weblog/', include('coltrane.urls.entries'),name='weblog'),
    url(r'^tiny_mce/(?P<path>.*)$', 'django.views.static.serve',
         { 'document_root': settings.PROJECT_ROOT + '/js/tiny_mce/' }),
    url(r'^search/$', 'cms.search.views.search'),

    url(r'^weblog/feeds/(?P<url>.*)/$',
        'django.contrib.syndication.views.Feed', {'feed_dict': feeds}
        ),

    url(r'^codeshare/', include('cab.urls.home')),
    url(r'^codeshare/snippets/', include('cab.urls.snippets')),
    url(r'^codeshare/languages/', include('cab.urls.languages')),
    url(r'^codeshare/popular/', include('cab.urls.popular')),
    url(r'^codeshare/tags/', include('cab.urls.tags')),
    url(r'^codeshare/bookmarks/', include('cab.urls.bookmarks')),
    url(r'^codeshare/ratings/', include('cab.urls.ratings')),

    url(r'^codeshare/signup/', include('cab.urls.signup')),


    url(r'^codeshare/css/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': os.path.join(settings.PROJECT_ROOT, '../cab', 'css') }),

    #url(r'', include(urls)),
    #url(r'', include('django.contrib.flatpages.urls')),


)
