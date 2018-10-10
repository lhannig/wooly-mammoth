from django import forms
from django.forms import formset_factory

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
                  'weight',
                  'yarn',
                  'color'
                  ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['color'].queryset = Color.objects.none()

        if 'yarn' in self.data:
            try:
                yarn_id = int(self.data.get('yarn'))
                self.fields['color'].queryset = Color.objects.filter(yarntype=yarn_id).order_by('color')
            except (ValueError, TypeError):
                pass

        elif self.instance.pk:
            self.fields['color'].queryset = self.instance.yarn.coler_set.order_by('color')






