from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, DeleteView, TemplateView
from app.forms import PersonaForm,EmailForm
from app.models import Persona, Email
# Create your views here.

class CreatePersonaView(CreateView):
    """Create a new persona."""

    template_name = 'app/AppAddPersona.html'
    form_class = PersonaForm
    success_url = reverse_lazy('app:list_persona')

class ListPersonaView(TemplateView):

    template_name = 'app/AppListPersona.html'

    def get_context_data(self,*args,**kwargs):
        persona = Persona.objects.all()
        email = Email.objects.all()
        return {'persona': persona, 'email': email}
    