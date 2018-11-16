from django import forms
from django.forms import Textarea
from django.forms import formset_factory
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, HTML, Div
from crispy_forms.bootstrap import FieldWithButtons, Field, InlineField

from .models import Color, Yarn, Projectidea, FinishedObject, Manufacturer, Yarnshop, Swatch, Material

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
        widgets = {
            'notes': Textarea(attrs={'cols': 80, 'rows': 5}),
        }

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))
        self.helper.form_action = 'add_color'
        self.helper.form_id = 'colorform'
        self.helper.layout = Layout(
            Fieldset(
                'Enter color properties',
                'color',
                'col_nr',
                'quantity',
                'notes',
                Div(
                    Div(
                        Div(
                            Div(
                                Field('yarnshop'), css_class="col-lg-10"),
                            Div(
                                HTML("""<div><label>Missing?</label>
                                <button href="{% url 'add_yarnshop_modal' %}" type="button" data-toggle="modal"
                                data-target="#ColorModal" id="yarnshopModalButton" class="btn btn-info btn-sm"
                                role="button">Add Yarnshop!</button></div>
                                """), css_class="col-lg-2 text-center"
                            ),
                        ),
                        css_class="row no-gutters"),
                    css_class="container-fluid"),

            ),
        )
        super(ColorForm, self).__init__(*args, **kwargs)


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
        widgets = {
            'notes': Textarea(attrs={'cols': 80, 'rows': 5}),
        }

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))
        self.helper.form_action = 'add_yarn'
        self.helper.form_id = 'yarnform'
        self.helper.layout = Layout(
            Fieldset(
                'Enter yarn properties',
                'name',
                'superwash',
                'notes',
                Div(
                    Div(
                        Div(
                            Div(
                                Field('manufacturer'),
                                css_class="col-lg-10"),
                            Div(
                                HTML("""<div><label>Missing?</label>
                                    <button href="{% url 'add_manufacturer_modal' %}" type="button" data-toggle="modal" data-target="#YarnModal"
                                     id="manufacturerModalButton"                          
                                    class="btn btn-info btn-sm "                                                                      
                                    role="button">Add!</button></div>                                                                                                             
                                    """), css_class="col-lg-2 text-center"
                                ),
                            
                           ),
                        css_class="row no-gutters"),
                    css_class="container-fluid"),
                'wash',
                'weight',
                Div(
                    Div(
                        Div(
                            Div(
                                Field('materials'), css_class="col-lg-10"),
                            Div(
                                HTML("""<div><label>Missing?</label>
                                    <button href="{% url 'add_material_modal' %}" type="button" data-toggle="modal" data-target="#YarnModal"
                                     id="materialModalButton" class="btn btn-info btn-sm" 
                                    role="button">Add!</button></div>"""), css_class="col-lg-2 text-center"
                                )
                           ),
                        css_class="row no-gutters"),
                    css_class="container-fluid"),
            ),

        )
        super(YarnForm, self).__init__(*args, **kwargs)


class YarnForm2(forms.ModelForm):
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
        widgets = {
            'notes': Textarea(attrs={'cols': 80, 'rows': 5}),
        }

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))
        self.helper.form_action = 'add_yarn'
        self.helper.form_id = 'yarnform'
        self.helper.layout = Layout(
            Fieldset(
                'Enter yarn properties',
                'name',
                'superwash',
                'notes',
                Div(
                    Div(
                        Div(
                            Div(
                                Field('manufacturer'),
                                css_class="col-lg-10"),
                            Div(
                                HTML("""<div><label>Missing?</label>
                                    <button href="{% url 'add_manufacturer_modal' %}" type="button" data-toggle="modal" data-target="#ProjectideaModal2"
                                     id="manufacturerModalButton"                          
                                    class="btn btn-info btn-sm "                                                                      
                                    role="button">Add this!</button></div>                                                                                                             
                                    """), css_class="col-lg-2 text-center"
                            ),

                        ),
                        css_class="row no-gutters"),
                    css_class="container-fluid"),
                'wash',
                'weight',
                Div(
                    Div(
                        Div(
                            Div(
                                Field('materials'), css_class="col-lg-10"),
                            Div(
                                HTML("""<div><label>Missing?</label>
                                    <button href="{% url 'add_material_modal' %}" type="button" data-toggle="modal" data-target="#ProjectideaModal2"
                                     id="materialModalButton" class="btn btn-info btn-sm" 
                                    role="button">Add this!</button></div>"""), css_class="col-lg-2 text-center"
                            )
                        ),
                        css_class="row no-gutters"),
                    css_class="container-fluid"),
            ),

        )
        super(YarnForm2, self).__init__(*args, **kwargs)


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
        widgets = {
            'notes': Textarea(attrs={'cols': 80, 'rows': 5}),
        }

    def __init__(self, *args, **kwargs):

        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))
        self.helper.form_action = 'add_projectidea'
        self.helper.layout = Layout(
            Fieldset('Properties',
                     'name',
                     'notes',
                     'yardage_needed',
                     'skeins_needed',
                     'weight',
                     Div(
                         Div(
                             Div(
                                 Div(
                                     Field('yarn'), css_class="col-lg-10"),
                                 Div(
                                     HTML("""<div><label>Missing?</label>
                                    <button href="{% url 'add_yarn_modal' %}" type="button" data-toggle="modal" data-target="#ProjectideaModal"
                                     id="projectideaModalButton" class="btn btn-info btn-sm" 
                                    role="button">Add!</button></div>"""), css_class="col-lg-2 text-center"
                                 )
                             ),
                             css_class="row no-gutters"),
                         css_class="container-fluid"),
                     ),
                        'color',
        )
        super(ProjectideaForm, self).__init__(*args, **kwargs)


        super().__init__(*args, **kwargs)
        self.fields['color'].queryset = Color.objects.none()

        if 'yarn' in self.data:
            try:
                yarn_id = int(self.data.get('yarn'))
                self.fields['color'].queryset = Color.objects.filter(yarntype=yarn_id).order_by('color')
            except (ValueError, TypeError):
                pass

        elif self.instance.pk:
            self.fields['color'].queryset = self.instance.yarn.color_set.order_by('color')




class FinishedObjectForm(forms.ModelForm):
    """add a new finished object"""
    class Meta:
        model = FinishedObject
        fields = ['name',
                  'projectidea',
                  'recipient',
                  'stichnr',
                  'notes',
                  'yarn',
                  'color',
                  'skeins_used',
                  'needlesize',
                  ]

        widgets = {
            'notes': Textarea(attrs={'cols': 80, 'rows': 5}),
            }

    def __init__(self, *args, **kwargs):

        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))
        self.helper.form_action = 'finished'
        self.helper.layout = Layout(
            Fieldset('Properties',
                     'name',
                     'projectidea',
                     'recipient',
                     'stichnr',
                     'notes',
                     'yarn',
                     'color',
                     'skeins_used',
                     'needlesize'
                     ),

        )
        super(FinishedObjectForm, self).__init__(*args, **kwargs)

        super().__init__(*args, **kwargs)
        self.fields['color'].queryset = Color.objects.none()

        if 'yarn' in self.data:
            try:
                yarn_id = int(self.data.get('yarn'))
                self.fields['color'].queryset = Color.objects.filter(
                    yarntype=yarn_id).order_by('color')
            except (ValueError, TypeError):
                pass

        elif self.instance.pk:
            self.fields[
                'color'].queryset = self.instance.yarn.color_set.order_by(
                'color')







class ManufacturerForm(forms.ModelForm):
    """create a new Manufacturer"""
    class Meta:
        model = Manufacturer
        fields = ['name']

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))
        self.helper.form_id = 'manufacturerform'
        self.helper.form_action = 'add_manufacturer'
        self.helper.layout = Layout(
            Fieldset(
                    '',
                    'name'))
        super(ManufacturerForm, self).__init__(*args, **kwargs)





class YarnshopForm(forms.ModelForm):
    """create a new yarnshop"""
    class Meta:
        model = Yarnshop
        fields = ['name',
                  'notes']
        widgets = {
            'notes': Textarea(attrs={'cols': 80, 'rows': 5}),
        }

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper. add_input(Submit('submit', 'Submit'))
        self.helper.form_id = 'yarnshopform'
        self.helper.form_action = 'add_yarnshop'
        self.helper.layout = Layout(
            Fieldset(
                '',
                'name',
                'notes'
            )
        )
        super(YarnshopForm, self).__init__(*args, **kwargs)

class SwatchForm(forms.ModelForm):
    """create a new swatch"""
    class Meta:
        model = Swatch
        fields = ['name',
                  'n_rows',
                  'n_stitches',
                  'n_rows_washed',
                  'n_stitches_washed',
                  'needlesize',
                  'yarn',
                  'notes']
        widgets = {
            'notes': Textarea(attrs={'cols': 80, 'rows': 5}),
        }

class MaterialForm(forms.ModelForm):
    """create a new Material"""
    class Meta:
        model = Material
        fields = ['name', 'notes']
        widgets = {
            'notes': Textarea(attrs={'cols': 80, 'rows': 5}),
        }

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))
        self.helper.form_action = 'add_material'
        self.helper.form_id = 'materialform'
        self.helper.layout = Layout(
            Fieldset(
                    '',
                    'name',
                    'notes'))
        super(MaterialForm, self).__init__(*args, **kwargs)


