from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render_to_response
from django.contrib.auth.decorators import login_required
from cab.models import Bookmark, Snippet
from django.views.generic.list import ListView
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
from django.core.context_processors import csrf

from dbgp.client import brk

def add_bookmark(request, snippet_id):
    snippet = get_object_or_404(Snippet, pk=snippet_id)
    try:
        Bookmark.objects.get(user__pk=request.user.id, snippet__pk=snippet_id)
    except Bookmark.DoesNotExist:
        bookmark = Bookmark.objects.create(user=request.user, snippet=snippet)
    return HttpResponseRedirect(snippet.get_absolute_url())
add_bookmark = login_required(add_bookmark)

@csrf_protect
def delete_bookmark(request, snippet_id):
    #brk(host='127.0.0.1', port=53891)
    if request.method == 'POST':
        snippet = get_object_or_404(Snippet, pk=snippet_id)
        Bookmark.objects.filter(user__pk=request.user.id, snippet__pk=snippet.id).delete()
        return HttpResponseRedirect(snippet.get_absolute_url())
    else:
        #c = { 'snippet': snippet}
	c={}
        c.update(csrf(request))
        return render_to_response('cab/confirm_bookmark_delete.html',
                                    c,
                                    context_instance=RequestContext(request))
delete_bookmark = login_required(delete_bookmark)

class UserBookMarkListView(ListView):
    paginate_by = 20
    template_name='cab/user_bookmarks.html'

    def get_queryset(self):
        return Bookmark.objects.filter(user__pk=self.request.user.id)

