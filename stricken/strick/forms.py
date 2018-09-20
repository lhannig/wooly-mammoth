from django import forms
from django.core.exceptions import ValidationError
from .models import Color

class RenewNrinStash(forms.ModelForm):

    class Meta:
        model = Color
        fields = ['yarntype', 'nr_in_stash']


