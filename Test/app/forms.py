from django import forms
from app.models import Persona, Email

class PersonaForm(forms.ModelForm):

    class Meta:
        """Form settings."""

        model = Persona
        fields = ('Name','PathernalLastName', 'MathernalLastName','Edad','Sexo', 'Cedula')


class EmailForm(forms.ModelForm):

    class Meta:
        """Form settings."""

        model = Email
        fields = ('persona','Email','Orden')