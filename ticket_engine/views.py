from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponseRedirect
from ticket_engine.models import Ticket
from django.template import RequestContext
from ticket_engine.forms import TicketForm
from intra.views import get_ctx

# Create your views here.

def accueil(request):
    user_ctx = get_ctx(request)
    try:
        print len(user_ctx)
    except TypeError:
        return redirect('/login/')
    ctx = {'user_is_logged_in': user_ctx}
    user = ctx['user_is_logged_in'][0][2]
    tick = Ticket.objects.filter(user=user)
    return render(request, 'ticket_engine/accueil.html', { 'ticket': tick, 'user_is_logged_in' : user_ctx })


def create_ticket(request):
    user_ctx = get_ctx(request)
    try:
        print len(user_ctx)
    except TypeError:
        return redirect('/login/')
    ctx = {'user_is_logged_in': user_ctx}
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title'] 
            content = form.cleaned_data['content']
            priority = form.cleaned_data['priority']
            status = form.cleaned_data['status']
            queue = form.cleaned_data['queue']
            pub_date = form.cleaned_data['pub_date']
            user = form.cleaned_data['user']
            post = True
            form.save()
            return HttpResponseRedirect('/ticket/')
    else:
        form = TicketForm()
    return render_to_response('ticket_engine/create.html', { 'ctx': ctx }, RequestContext(request, locals()))

def detail(request, ticket_id):
    tick = Ticket.objects.filter(id=ticket_id)
    return render(request, 'ticket_engine/accueil_admin.html', { 'ticket': tick, 'ticket_id': ticket_id })