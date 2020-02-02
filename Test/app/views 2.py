from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, DeleteView
from app.forms import PersonaForm,EmailForm
from app.models import Persona, Email
from django.forms import modelformset_factory, inlineformset_factory
# Create your views here.

class CreatePersonaView(CreateView):
    """Create a new persona."""

    template_name = 'app/AddPersona.html'
    form_class = PersonaForm
    success_url = reverse_lazy('app:index')



def index(request, persona_id):
    persona = Persona.objects.get(pk=persona_id)
    #LanguageFormset = modelformset_factory(Language, fields=('name',))
    EmailFormset = inlineformset_factory(Persona, Email, fields=('Email','Jerarquia'), can_delete=False, extra=1)

    if request.method == 'POST':
        #formset = LanguageFormset(request.POST, queryset=Language.objects.filter(programmer__id=programmer.id))
        formset = EmailFormset(request.POST, instance=persona)
        if formset.is_valid():
            formset.save()
            #instances = formset.save(commit=False)
            #for instance in instances:
            #    instance.programmer_id = programmer.id 
            #    instance.save()

            return redirect('index', persona_id=persona.id)

    #formset = LanguageFormset(queryset=Language.objects.filter(programmer__id=programmer.id))
    formset = EmailFormset(instance=persona)

    return render(request, 'app/index.html', {'formset' : formset})