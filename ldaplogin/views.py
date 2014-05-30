from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.template import RequestContext
from Auth42.auth42 import Auth42
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout
from django.http import HttpResponseRedirect

def login_view(request):
    c = {}
    c.update(csrf(request))
    if request.user.is_authenticated():
        return render_to_response('home.html',  context_instance = RequestContext(request))
    elif request.method == "POST":
        username = request.POST["login_user"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                return render_to_response('home.html', context_instance = RequestContext(request))
        ldap = Auth42()
        if ldap is not None and ldap.ldap_authenticate(username, password):
            request.session[0] = username
            request.session[1] = password
            request.session["login"] = username
            request.session["password"] = password
            return HttpResponseRedirect('/')

    return render_to_response("login_page.html", context_instance=RequestContext(request))

def logout_view(request):
    logout(request)
    request.session[0] = None
    request.session[1] = None
    return HttpResponseRedirect('/login/')


