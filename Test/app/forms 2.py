from django import forms
from app.models import Persona, Email
from django.forms import ModelForm


class PersonaForm(forms.ModelForm):

    class Meta:
        """Form settings."""

        model = Persona
        fields = '__all__'


class EmailForm(forms.ModelForm):

    class Meta:
        """Form settings."""

        model = Email
        fields = '__all__'

