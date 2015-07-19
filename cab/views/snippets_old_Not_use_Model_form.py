from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from cab.forms import AddSnippetForm


def add_snippet(request):

	if request.method == 'POST':
		form = AddSnippetForm(author=request.user, data=request.POST)
		if form.is_valid():
			new_snippet = form.save()
			return HttpResponseRedirect(new_snippet.get_absolute_url())
	else:
		form = AddSnippetForm(author=request.user)
		c = { 'form': form }
		c.update(csrf(request))

		return render_to_response('cab/add_snippet.html',
					c )
add_snippet = login_required(add_snippet)
        