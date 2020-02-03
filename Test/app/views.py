from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, DeleteView, TemplateView, UpdateView
from app.forms import PersonaForm,EmailForm
from app.models import Persona, Email
from django.db.models import Q
# Create your views here.



class CreatePersonaView(CreateView):
    """Creación de una nueva persona."""

    template_name = 'app/AppAddPersona.html'
    form_class = PersonaForm
    success_url = reverse_lazy('app:list_persona')

class ListPersonaView(TemplateView):
    """Enlista las  personas y correos existentes."""


    template_name = 'app/AppListPersona.html'


    def get_object(self, request):
        queryset = request.GET.get("buscar")
        if queryset:
            email = Email.objects.filter(
                Q(Email_icontains = queryset )
            ).distinct()
        return render(request,'app/AppListPersona.html',{'email': email})


    def get_context_data(self,*args,**kwargs):
        persona = Persona.objects.all()
        email = Email.objects.all()
        return {'persona': persona, 'email': email}



class DetailPersonaView(DetailView):
    """Visualiza los detalles de la  persona seleccionada ."""

   
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
        """Elimina a la persona seleccionada."""

    
    template_name = 'app/AppDeletePersona.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Persona,id=id_)

    def get_success_url(self):

        return reverse('app:list_persona')

    
class CreateEmailView(CreateView):
    """Creación de un nuevo correo."""

    template_name = 'app/AppAddEmail.html'
    form_class = EmailForm
    success_url = reverse_lazy('app:list_persona')


class UpdateEmailView( UpdateView):
    """Genera el orden de los correos administrado por el ususario."""

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
    """Actualiza los datos del usuario seleccionado ."""

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