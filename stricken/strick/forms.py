from django import forms

from .models import Color, Yarn

class ColorForm(forms.ModelForm):
    class Meta:
        model = Color
        fields = ['yarntype',
                  'color',
                  'col_nr',
                  'own_it',
                  'quantity',
                  'notes',
                  'yarnshop',
                  ]



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



