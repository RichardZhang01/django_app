from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Participant


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ('email', 'firstName', 'lastName')
        labels = {
            'firstName': _('First Name'),
            'lastName': _('Last Name'),
        }
