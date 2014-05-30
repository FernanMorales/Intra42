from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from ldaplogin.Auth42.auth42 import Auth42
from django.core.context_processors import csrf
from annuaire.models import Student


def home(request):
    c = {}
    c.update(csrf(request))
    ldap = Auth42()
    ctx = None
    if request.user.is_anonymous():
        if ldap is None or 'login' not in request.session or 'password' not in request.session:
            return redirect('/login/')
        if not ldap.ldap_authenticate(request.session["login"], request.session["password"]):
            return redirect('/login/')
    try:
        user_list = Student.objects.all().values_list('firstname', 'lastname', 'login').filter(login=request.session["login"])
        print user_list
        ctx = {'user_is_logged_in': user_list}
    except KeyError:
        pass
    print ctx
    return render_to_response("home.html", ctx,  context_instance = RequestContext(request))


def is_logged_in(request):
    ldap = Auth42()
    print request.session["login"] + ' ' + request.session["password"]
    if ldap is not None and ldap.ldap_authenticate(request.session["login"], request.session["password"]):
        return True
    return False


def get_ctx(request):
    c = {}
    c.update(csrf(request))
    ldap = Auth42()
    if request.user.is_anonymous():
        if ldap is None or 'login' not in request.session or 'password' not in request.session:
            return redirect('/login/')
        if not ldap.ldap_authenticate(request.session["login"], request.session["password"]):
            return redirect('/login/')
    try:
        return Student.objects.all().values_list('firstname', 'lastname', 'login').filter(login=request.session["login"])
    except KeyError:
        pass
    return request.user
