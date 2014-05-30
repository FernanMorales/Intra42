from django.shortcuts import render_to_response
from django.template import RequestContext
from intra.views import get_ctx


def calendar(request):
    user_ctx = get_ctx(request)
    ctx = {'user_is_logged_in': user_ctx}
    return render_to_response('planning.html', ctx, context_instance = RequestContext(request))



