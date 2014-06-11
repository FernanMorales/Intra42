from annuaire.models import Student
from django.template import RequestContext
from intra.views import get_ctx
from django.shortcuts import render_to_response, redirect


def user_profile(request, username):
    user_ctx = get_ctx(request)
    try:
        print len(user_ctx)
    except TypeError:
        return redirect('/login/')
    field = Student.objects.all().values_list('login', 'firstname', 'lastname').filter(login=username)
    ctx = {'field':field, 'username':username, 'user_is_logged_in': user_ctx}
    return render_to_response('profil.html', ctx, context_instance = RequestContext(request))



