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

class DeletePersonaView( DeleteView):
    
    template_name = 'app/AppDeletePersona.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Persona,id=id_)

    def get_success_url(self):

        return reverse('app:list_persona')

    
class CreateEmailView(CreateView):
    """Create a new Email."""

    template_name = 'app/AppAddEmail.html'
    form_class = EmailForm
    success_url = reverse_lazy('app:list_persona')