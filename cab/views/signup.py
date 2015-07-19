from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from cab.forms_adduser import SignupForm


def signup(request):
    if request.method == 'POST':
        form = SignupForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/accounts/login/")
    else:
        form = SignupForm()
	c = { 'form': form }
	c.update(csrf(request))
        return render_to_response('cab/signup.html', c )
