from django import forms

from .models import Color, Yarn

class ColorForm(forms.ModelForm):
    class Meta:
        model = Color
        fields = ['nr_in_stash', ]



class YarnForm(forms.ModelForm):
    class Meta:
        model = Yarn
        fields = ['name',
                  'superwash',
                  'notes',
                  'manufacturer',
                  'wash',
                  'weight',
                  'materials',
                  ]



