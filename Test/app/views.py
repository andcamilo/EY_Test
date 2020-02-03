from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, DeleteView, TemplateView, UpdateView
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



class DetailPersonaView(DetailView):
   
    template_name = 'app/AppDetailPersona.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Persona, id=id_)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id = self.kwargs.get("id")
        context['Persona'] = Persona.objects.filter(id=id)
        context['Email'] = Email.objects.all()
        return context

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


class UpdateEmailView( UpdateView):
    """Update Email view."""

    template_name = 'app/AppUpdateEmail.html'
    model = Email
    fields = ['Email', 'Orden']


    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Email, id=id_)

    def get_success_url(self):
        """Return to user's profile."""
        id_ = self.object.id
        return reverse('app:list_persona')


class UpdatePersonalView(UpdateView):
    """Update Personal view."""

    template_name = 'app/AppUpdatePersona.html'
    model = Persona
    fields = ['Name', 'PathernalLastName', 'MathernalLastName','Cedula','Edad','Sexo']


    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Persona, id=id_)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id = self.kwargs.get("id")
        context['Persona'] = Persona.objects.filter(id=id)
        context['Email'] = Email.objects.all()
        return context

    def get_success_url(self):
        """Return to user's profile."""
        id_ = self.object.id
        return reverse('app:list_persona')