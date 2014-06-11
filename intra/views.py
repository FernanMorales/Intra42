from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from ldaplogin.Auth42.auth42 import Auth42
from django.core.context_processors import csrf
from annuaire.models import Student
from ftadmin.models import Activite


def home(request):
    user_ctx = get_ctx(request)
    try:
        print len(user_ctx)
    except TypeError:
        return redirect('/login/')
    activites = Activite.objects.all().values_list('module', 'name', 'date_acti_debut', 'date_acti_fin',
        'date_insc_debut', 'date_insc_fin').order_by('id')
    ctx = {'user_is_logged_in': user_ctx, 'activites': activites}
    return render_to_response('home.html', ctx, context_instance = RequestContext(request))


def is_logged_in(request):
    ldap = Auth42()
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
        return redirect('/login/')
    return request.user
