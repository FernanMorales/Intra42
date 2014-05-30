from django.shortcuts import render_to_response
from django.template import RequestContext
from ftadmin.models import Module, Activite
from intra.views import get_ctx


def home(request):
    user_ctx = get_ctx(request)

    modules = Module.objects.all().values_list('name', 'id', 'nb_credit', 'nb_place').order_by('id')
    activites = Activite.objects.all().values_list('name', 'module')

    print activites

    ctx = {'modules':modules, 'activites':activites, 'user_is_logged_in': user_ctx}

    return render_to_response('elearning.html', ctx, context_instance = RequestContext(request))
