from django import forms
from app.models import Profile, Email

class ProfileForm(forms.ModelForm):

    class Meta:
        """Form settings."""

        model = Profile
        fields = ('user','PathernalLastName', 'MathernalLastName','Edad','Sexo', 'Cedula')


class EmailForm(forms.ModelForm):

    class Meta:
        """Form settings."""

        model = Email
        fields = ('profile','Email')

