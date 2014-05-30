from django.shortcuts import render_to_response, redirect
from models import Student
from django.template import RequestContext
from intra.views import get_ctx

def users(request):
    user_ctx = get_ctx(request)

    user_list = Student.objects.all().values_list('login', 'firstname', 'lastname', 'photo').order_by('login')

    ctx = {'user_list':user_list, 'user_is_logged_in': user_ctx}

    return render_to_response('annuaire.html', ctx, context_instance = RequestContext(request))
