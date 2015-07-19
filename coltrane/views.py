from django.shortcuts import get_object_or_404, render_to_response
from django.views.generic.detail import DetailView
from django.views.generic import ListView

from coltrane.models import Entry,Link,Category

# Hugh uncomment it
from dbgp.client import brk


def entries_index(request):
    return render_to_response('coltrane/entry_index.html',
        { 'entry_list': Entry.objects.all() })

def link_archive_index(request):
    return render_to_response('coltrane/link_archive_index.html',
        { 'link_list': Link.objects.all() })

def category_list(request):
    return render_to_response('coltrane/category_list.html',
        { 'object_list': Category.objects.all() })

#def category_detail(request, slug):
#    category = get_object_or_404(Category, slug=slug)
#    return render_to_response('coltrane/category_detail.html',
#                              {'object_list': category.entry_set.all(), 'category': category})

class CategoryDetailView(ListView):
    template_name = 'coltrane/category_entry_index.html'
    
    def get_queryset(self):
        #brk(host="localhost",port=53891)
        category = get_object_or_404(Category,slug=self.kwargs['slug'])
        self.category = category
        return category.entry_set.all()
    
    def get_context_data(self, **kwargs):
        context=super(CategoryDetailView, self).get_context_data(**kwargs)
        #brk(host="localhost",port=53891)
        context['category'] = self.category
        #'category': category
        return context

class TaggedListView(ListView):
    template_name =  'coltrane/entries_by_tag.html'

    def get_queryset(self):
        #brk(host="localhost",port=53891)
        tag = get_object_or_404(Entry,tag=self.kwargs['tag'])
        self.category = category
        return category.entry_set.all()
