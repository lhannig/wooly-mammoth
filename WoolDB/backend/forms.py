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
                'Color properties',
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
                                <button type="button" data-toggle="collapse" data-target="#yarnshopdiv" onclick="load_yarnshopform()"
                                 id="yarnshopModalButton" class="btn btn-info btn-sm"
                                role="button">Add!</button></div>
                                """), css_class="col-lg-2 text-center"
                            ),

                        ), Div(id='yarnshopdiv', css_class="collapse col-lg-12",),
                        css_class="row no-gutters"),
                    css_class="container-fluid"),

            ),
        )

        super(ColorForm, self).__init__(*args, **kwargs)
        self.fields['col_nr'].label = 'Color Number'


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
                'Yarn properties!',
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
                                    <button  type="button" 
                                     id="manufacturerModalButton"   data-toggle="collapse" data-target="#manufacturerdiv" onclick="load_manufacturerform()"                       
                                    class="btn btn-info btn-sm "                                                                      
                                    role="button">Add!</button></div>                                                                                                             
                                    """), css_class="col-lg-2 text-center"
                                ),
                            
                           ),Div(id='manufacturerdiv', css_class="collapse col-lg-12",),
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
                                    <button type="button" data-toggle="collapse" data-target="#materialsdiv" onclick="load_materialform()"
                                     id="materialModalButton" class="btn btn-info btn-sm" 
                                    role="button">Add!</button></div>"""), css_class="col-lg-2 text-center"
                                )
                           ),Div(id='materialsdiv', css_class="collapse col-lg-12",),
                        css_class="row no-gutters"),
                    css_class="container-fluid"),
            ),

        )
        super(YarnForm, self).__init__(*args, **kwargs)





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
            Fieldset('Projectidea properties',
                     'name',
                     'link',
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
                                    <button  type="button" 
                                     id="projectideaYarnModalButton" class="btn btn-info btn-sm" 
                                    role="button">Add!</button></div>"""), css_class="col-lg-2 text-center"
                                 )
                             ),
                             css_class="row no-gutters"),
                         css_class="container-fluid"),
                     ),
            Div(
                Div(
                    Div(
                        Div(
                            Field('color'), css_class="col-lg-10"),
                        Div(
                            HTML("""<div><label>Missing?</label>
                                <button  type="button" 
                                id="projectideaColorModalButton" class="btn btn-info btn-sm" 
                                ole="button">Add!</button></div>"""),
                            css_class="col-lg-2 text-center"
                        )
                    ),
                    css_class="row no-gutters"),
                css_class="container-fluid"),
        )

        super(ProjectideaForm, self).__init__(*args, **kwargs)
        self.fields['skeins_needed'].label = 'Number of skeins needed'


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



class ProjectideaForm2(forms.ModelForm):
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
            Fieldset('Projectidea properties',
                     'name',
                     'notes',
                     'yardage_needed',
                     'skeins_needed',
                     'weight',
                     'yarn',
                     'color'
                     ))

        super(ProjectideaForm2, self).__init__(*args, **kwargs)
        self.fields['skeins_needed'].label = 'Number of skeins needed'

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
            Fieldset('Finished object properties',
                     'name',
                       Div(
                    Div(
                        Div(
                            Div(
                                Field('projectidea'), css_class="col-lg-10"),
                                Div(
                                    HTML("""<div><label>Missing?</label>
                                    <button  type="button" 
                                     id="finishedobjectProjectideaModalButton" class="btn btn-info btn-sm" 
                                    role="button">Add!</button></div>"""), css_class="col-lg-2 text-center"
                                 )
                             ),
                             css_class="row no-gutters"),
                         css_class="container-fluid"),
                     'recipient',
                     'stichnr',
                     'notes',
                      Div(
                    Div(
                        Div(
                            Div(
                                Field('yarn'), css_class="col-lg-10"),
                                Div(
                                    HTML("""<div><label>Missing?</label>
                                    <button  type="button" 
                                     id="finishedobjectYarnModalButton" class="btn btn-info btn-sm" 
                                    role="button">Add!</button></div>"""), css_class="col-lg-2 text-center"
                                 )
                             ),
                             css_class="row no-gutters"),
                         css_class="container-fluid"),
                         Div(
                    Div(
                        Div(
                            Div(
                                Field('color'), css_class="col-lg-10"),
                                Div(
                                    HTML("""<div><label>Missing?</label>
                                    <button  type="button" 
                                     id="finishedobjectColorModalButton" class="btn btn-info btn-sm" 
                                    role="button">Add!</button></div>"""), css_class="col-lg-2 text-center"
                                 )
                             ),
                             css_class="row no-gutters"),
                         css_class="container-fluid"),
                     'skeins_used',
                     'needlesize'
                     ),

        )
        super(FinishedObjectForm, self).__init__(*args, **kwargs)
        self.fields['skeins_used'].label = 'Number of used skeins'
        self.fields['stichnr'].label = 'Number of stitches'

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
            self.fields['color'].queryset = self.instance.yarn.color_set.order_by('color')







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
                    'Manufacturer properties',
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
        self.helper.add_input(Submit('submit', 'Submit'))
        self.helper.form_id = 'yarnshopform'
        self.helper.form_action = 'add_yarnshop'
        self.helper.layout = Layout(
            Fieldset(
                'Yarnshop properties',
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

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))
        self.helper.form_action = 'add_swatch'
        self.helper.layout = Layout(
            Fieldset(
                'Add a new swatch!',
                'name',
                'n_rows',
                'n_stitches',
                'n_rows_washed',
                'n_stitches_washed',
                'needlesize',
                 Div(
                        Div(
                            Div(
                                Field('yarn'), css_class="col-lg-10"),
                                Div(
                                    HTML("""<div><label>Missing?</label>
                                    <button  type="button" 
                                     id="swatchYarnModalButton" class="btn btn-info btn-sm" 
                                    role="button">Add!</button></div>"""), css_class="col-lg-2 text-center"
                                 )
                             ),
                             css_class="row no-gutters"),
                         css_class="container-fluid"),
                'notes'
            )

        super(SwatchForm, self).__init__(*args, **kwargs)
        self.fields['n_rows'].label = 'Number of rows'
        self.fields['n_stitches'].label = 'Number of stitches'
        self.fields['n_rows_washed'].label = 'Number of rows after washing'
        self.fields['n_stitches_washed'].label = 'Number of stitches after washing'

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
                    'Material properties',
                    'name',
                    'notes'))
        super(MaterialForm, self).__init__(*args, **kwargs)


