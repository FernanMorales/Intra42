from django.shortcuts import render_to_response, redirect
from models import Module, Activite
from django.template import RequestContext
from django.forms import ModelForm

def home(request):
    if request.user.is_anonymous():
        ''' OR IF USER IS NOT AN ADMIN'''
        return redirect('/login/')
    if request.user.is_anonymous():
        return redirect('/login/')
    modules = Module.objects.all().values_list('name', 'id', 'nb_credit', 'nb_place').order_by('id')
    activites = Activite.objects.all().values_list('name', 'id', 'type', 'module').order_by('id')

    ctx = {'modules':modules, 'activites':activites}

    return render_to_response('ftadmin-panel.html', ctx, context_instance = RequestContext(request))

def create(request):
    if request.user.is_anonymous():
        ''' OR IF USER IS NOT AN ADMIN'''
        return redirect('/login/')
    return

def rud_module(request, module):
    if request.user.is_anonymous():
        ''' OR IF USER IS NOT AN ADMIN'''
        return redirect('/login/')
    form = ModuleForm(instance=module)
    return render_to_response('rud.html', form, context_instance = RequestContext(request))

class ModuleForm(ModelForm):
     class Meta:
         model = Module
         fields = ['name', 'description', 'nb_place', 'date_insc_debut', 'date_insc_fin', 'date_mod_debut',
                   'date_mod_fin', 'nb_credit']
