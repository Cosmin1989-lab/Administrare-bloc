from django import forms
from .models import Locatar, Apartament, Factura

class LocatarForm(forms.ModelForm):
    class Meta:
        model = Locatar
        fields = ['nume', 'apartament']

class ApartamentForm(forms.ModelForm):
    class Meta:
        model = Apartament
        fields = ['numar']

class FacturaForm(forms.ModelForm):
    class Meta:
        model = Factura
        fields = ['locatar', 'suma', 'data']

from django import forms
from django.contrib.auth.models import User

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Parolele nu se potrivesc.")

