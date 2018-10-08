from django import forms

from .models import Color, Yarn, Projectidea

class ColorForm(forms.ModelForm):
    """add/edit a colorway to a yarn"""
    class Meta:
        model = Color
        exclude = ('yarntype',)

        fields = ['color',
                  'col_nr',
                  'own_it',
                  'quantity',
                  'notes',
                  'yarnshop',
                  ]



class YarnForm(forms.ModelForm):
    """add/edit a yarntype"""
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



class ProjectideaForm(forms.ModelForm):
    """add/edit a projectidea"""
    class Meta:
        model = Projectidea
        fields = ['name',
                  'link',
                  'notes',
                  'yardage_needed',
                  'skeins_needed',
                  'yarn',
                  'color',
                  'weight',
                  ]
