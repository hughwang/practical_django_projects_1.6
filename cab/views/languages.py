from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from cab.models import Language

class SubListView(ListView):
    paginate_by = 20
    template_name='cab/language_detail.html'

    def get_queryset(self):
        language = get_object_or_404(Language,slug=self.kwargs['slug'])
        self.language = language
        return language.snippet_set.all()

    def get_context_data(self, **kwargs):
        context = super(self.__class__, self).get_context_data(**kwargs)
        context['language'] = self.language
        return context

#def language_detail(request, slug):
#    return  SubListView.as_view()