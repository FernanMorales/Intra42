from django.shortcuts import render_to_response, redirect
from models import Student
from django.template import RequestContext
from intra.views import get_ctx
from ldaplogin.Auth42 import auth42

def users(request):
    user_ctx = get_ctx(request)
    try:
        print len(user_ctx)
    except TypeError:
        return redirect('/login/')
    user_list = Student.objects.all().values_list('login', 'firstname', 'lastname').order_by('login')
    print user_list[0][0]

    ldap = auth42.Auth42()
    ctx = {'user_list':user_list, 'user_is_logged_in': user_ctx}

    return render_to_response('annuaire.html', ctx, context_instance = RequestContext(request))
