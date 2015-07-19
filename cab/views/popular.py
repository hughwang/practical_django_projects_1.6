from cab.models import Language, Snippet
from django.views.generic.list import ListView
from django.shortcuts import get_object_or_404


class TopAuthorListView(ListView):
    paginate_by = 20
    template_name='cab/top_authors.html'

    def get_queryset(self):
        return Snippet.objects.top_authors()

class TopLanguageListView(ListView):
    paginate_by = 20
    template_name='cab/top_languages.html'
    
    def get_queryset(self):
        return Language.objects.top_languages()


class MostBookMarkedListView(ListView):
    paginate_by = 20
    template_name='cab/most_bookmarked.html'
    
    def get_queryset(self):
        return Snippet.objects.most_bookmarked()

class TopRatedListView(ListView):
    paginate_by = 20
    template_name='cab/top_rated.html'
    
    def get_queryset(self):
        return Snippet.objects.top_rated(),

