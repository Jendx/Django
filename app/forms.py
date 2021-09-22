"""
Definition of forms.
"""
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from .models import Hraci, Servery, Bany, Bugy, Moderovani, Typy_banu, Typy_bugu, Formulare

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))

class BootstrapBanForm(forms.ModelForm):
    class Meta:
        model = Bany
        fields = ["ban_id", "hrac_id", "server_id", "typ_banu", "zabanovany", "datum_banu", "datum_odbanovani", "duvod"]

class BootstrapModerationForm(forms.ModelForm):
    class Meta:
        model = Moderovani
        fields = ["incident_id", "hrac_id", "server_id", "provineni", "postih", "datum_incidentu", "datum_odebrani_trestu"]

class BootstrapBugyForm(forms.ModelForm):
    class Meta:
        model = Bugy
        fields = ["bug_id", "hrac_id", "server_id", "typ_bugu", "vyreseny", "popis", "poskozeni"]

class BootstrapTypyBuguForm(forms.ModelForm):
    class Meta:
        model = Typy_bugu
        fields = ["bug_id", "bug_typ", "nazev", "popis"]

class BootstrapTypyBanuForm(forms.ModelForm):
    class Meta:
        model = Typy_banu
        fields = ["ban_id", "ban_typ", "nazev", "popis"]

class BootstrapServeryForm(forms.ModelForm):
    class Meta:
        model = Servery
        fields = ["server_id", "nazev", "zeme", "ip", "game_port", "query_port"]

class BootstrapHraciForm(forms.ModelForm):
    class Meta:
        model = Hraci
        fields = ["hrac_id", "Prezdivka"]

class BootstrapFormulareForm(forms.ModelForm):
    class Meta:
        model = Formulare
        fields = ["form_id", "nazev"]

class BootstrapUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]

class BootstrapFormulareForm(forms.ModelForm):
    class Meta:
        model = Formulare
        fields = ["form_id", "nazev"]
                     