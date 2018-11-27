from itertools import islice, chain

from django.shortcuts import render, get_object_or_404, redirect
from django.core.exceptions import ValidationError
from django.http import Http404
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from crispy_forms.utils import render_crispy_form
from django.template.context_processors import csrf

import bleach

from backend.models import Yarn, Manufacturer, Material, Needlesize, Color, \
                          Projectidea, Weight, FinishedObject, Yarnshop, Swatch
from backend.forms import YarnForm, ColorForm, ProjectideaForm, FinishedObjectForm, ManufacturerForm,\
                        YarnshopForm, SwatchForm, MaterialForm, ProjectideaForm2

# Create your views here.

def index(request):
    """returns index site"""
    return render(request, 'backend/index.html')
    # template = loader.get_template('backend/index.html')
    # context = {}
    # return HttpResponse(template.render(context, request))


@login_required
def yarns(request):
    """shows all yarns in stash and yarns currently unstashed """

    yarns = Yarn.objects.filter(color__own_it=True).distinct() \
                        .order_by('manufacturer__name', 'name')

    unstashed_yarns = Yarn.objects.exclude(color__own_it=True).distinct() \
                                  .order_by('manufacturer__name', 'name')

    materials = Material.objects.all()
    colors = Color.objects.all()

    return render(request, 'backend/yarns.html', {
        'yarns': yarns,
        'materials': materials,
        'colors': colors,
        'unstashed_yarns': unstashed_yarns,
    })


@login_required
def yarn_detail(request, yarntype_id):
    """shows one single yarn type and its proberties"""
    colors = Color.objects.filter(yarntype=yarntype_id, own_it=True)
    yarn = Yarn.objects.get(pk=yarntype_id)

    return render(request, 'backend/yarn_detail.html', {
        'colors': colors,
        'yarn':yarn,
    })


@login_required
def delete_yarn(request, yarntype_id):
    """delete a yarntype from the database and all of its colors"""

    yarn = get_object_or_404(Yarn, pk=yarntype_id)
    yarn.delete()
    messages.info(request, 'The yarn %s was successfully deleted' %yarn.name)

    return redirect('yarns')


@login_required
def add_yarn(request):
    """Add a new yarn"""

    form = YarnForm(request.POST)
    manufacturerform = ManufacturerForm(request.POST)

    materialform = MaterialForm(request.POST)



    if request.method != "POST":
        return render(request, 'backend/add_yarn.html', {'form': form, 'manufacturerform': manufacturerform,
                                                         'materialform': materialform})

    else:
        if form.is_valid():
            yarn = form.save()

            return redirect('yarn_detail', yarntype_id=yarn.pk)

        else:
            return render(request, 'backend/add_yarn.html', {'form': form, 'manufacturerform': manufacturerform,
                                                             'materialform': materialform})


@login_required
def edit_yarn(request, yarntype_id):
    """edit an existing yarn type"""
    yarn = get_object_or_404(Yarn, id=yarntype_id)
    form = YarnForm(request.POST or None, instance=yarn)
    form.helper.form_action = 'edit'
    manufacturerform = ManufacturerForm(request.POST)
    materialform = MaterialForm(request.POST)
    if form.is_valid():
        form.save()

        return redirect('yarn_detail', yarntype_id=yarn.id)

    return render(request, 'backend/edit_yarn.html', {'form': form, 'manufacturerform': manufacturerform,
                                                      'materialform': materialform})


@login_required
def color_detail(request, yarntype_id, color_id):
    """shows one color of a specific yarn"""
    color = Color.objects.filter(yarntype_id=yarntype_id).get(pk=color_id)

    return render(request, 'backend/color.html', {'color': color,})


@login_required
def add_color(request, yarntype_id):
    """add a new color for an existing yarn type"""
    if request.method == 'POST':
        form = ColorForm(request.POST)
        if form.is_valid():

            color = form.save(commit=False)
            # check if color is already in db
            if Color.objects.filter(color=color.color,
                                    col_nr=color.col_nr,
                                    yarntype=yarntype_id):
                col = Color.objects.get(color=color.color,
                                        yarntype=yarntype_id )
                return redirect('edit_color', yarntype_id=col.yarntype.id,
                                color_id=col.id)


            yarn = Yarn.objects.get(pk=yarntype_id)
            color.yarntype = yarn
            if color.quantity > 0:
                color.own_it = True


            color.save()

            return redirect('color_detail',
                            yarntype_id=yarntype_id,
                            color_id=color.pk)

    else:
        form = ColorForm()

    return render(request, 'backend/add_color.html', {'form': form, })


@login_required
def edit_color(request, yarntype_id, color_id):
    """edit an existing color"""

    color = get_object_or_404(Color, pk=color_id)
    form = ColorForm(request.POST or None, instance=color)
    if form.is_valid():
        color.own_it = color.quantity > 0
        form.save()

        return redirect('color_detail',
                        yarntype_id=yarntype_id,
                        color_id=color.id)

    return render(request, 'backend/edit_color.html', {'form': form, })


@login_required
def delete_color(request, yarntype_id, color_id):
    """ delete a color from the db """
    color = get_object_or_404(Color, pk=color_id)
    color.delete()
    messages.info(request,
                  'The color %s was successfully deleted' % color.color)

    return redirect('yarn_detail', yarntype_id)


@login_required
def projectideas(request):
    """show all existing projectideas"""
    projectideas = Projectidea.objects.all()
    yarns = Yarn.objects.all()
    colors = Color.objects.all()
    weights = Weight.objects.all()

    return render(request, 'backend/projectideas.html', {
        'projectideas': projectideas,
        'yarns': yarns,
        'colors': colors,
        'weights': weights,
    })


@login_required
def add_projectidea(request):
    """add a new idea for a project"""
    yarnshopform = YarnshopForm()
    if request.method == 'POST':
        form = ProjectideaForm(request.POST)

        if form.is_valid():
            projectidea = form.save()

            return redirect('projectidea_detail',
                             projectidea_id=projectidea.pk)

    else:
        form = ProjectideaForm()

    return render(request, 'backend/add_projectidea.html', {'form': form, 'yarnshopform': yarnshopform},)


@login_required
def load_colors(request):
    """load colors depending on yarnchoice"""
    yarn_id = request.GET.get('yarn')
    colors = Color.objects.filter(yarntype=yarn_id).order_by('color')

    return render(request, 'backend/dropdownlist_colors.html',
                  {'colors': colors,})


@login_required
def projectidea_detail(request, projectidea_id):
    """display one projectidea"""
    projectidea = get_object_or_404(Projectidea, pk=projectidea_id)
    colors = Color.objects.filter(projectidea__id=projectidea_id)

    return render(request, 'backend/projectidea_detail.html', {
        'projectidea': projectidea,
        'colors': colors,
    })


@login_required
def delete_projectidea(request, projectidea_id):
    """remove a projectidea from db"""
    project = get_object_or_404(Projectidea, pk=projectidea_id)
    project.delete()
    messages.info(request,
                  'The projectidea %s was successfully deleted' % project.name)

    return redirect('projectideas')


@login_required
def edit_projectidea(request, projectidea_id):
    """edit an existing projectidea"""
  #  projectidea_id = request.POST.get('projectidea_id')
    instance = get_object_or_404(Projectidea, id=projectidea_id)


    form = ProjectideaForm(request.POST or None, instance=instance)
    form.helper.form_action = 'edit'
    if form.is_valid():
        form.save()

        return redirect('projectidea_detail', projectidea_id=instance.id)

    return render(request, 'backend/edit_projectidea.html', {'form': form})


@login_required
def finishedobjects(request):
    """show all finished objects"""
    finishedobjects = FinishedObject.objects.all()
    yarns = Yarn.objects.all()
    needlesizes = Needlesize.objects.all()
    colors = Color.objects.all()

    return render(request, 'backend/finishedobjects.html',
                  {'finishedobjects': finishedobjects, 'yarns':yarns,
                            'needlesizes': needlesizes, 'colors':colors},)

@login_required
def add_fo(request):
    """add a finished object"""

    if request.method == 'POST':
        form = FinishedObjectForm(request.POST)
        form.helper.form_action ='add'
        if form.is_valid():
            finishedobject = form.save()

            return redirect('finishedobject_detail',
                            finishedobject_id=finishedobject.pk)

    else:
        form = FinishedObjectForm()
        form.helper.form_action = 'add'

    return render(request, 'backend/add_finishedobject.html', {'form': form}, )


@login_required
def finishedobject_detail(request, finishedobject_id):
    """shows details of a selected finished object"""

    finishedobject = FinishedObject.objects.get(pk=finishedobject_id)
    colors = Color.objects.all()
    needlesizes = Needlesize.objects.all()

    return render(request, 'backend/finishedobject_detail.html',
                  {'finishedobject': finishedobject, 'colors': colors,
                   'needlesizes': needlesizes},)


@login_required
def delete_finishedobject(request, finishedobject_id):
    """delete a finished object"""

    fo = get_object_or_404(FinishedObject, pk=finishedobject_id)
    fo.delete()
    messages.info(request, 'The finished object %s was successfully deleted' % fo.name)

    return redirect('finishedobjects')


@login_required
def edit_fo(request, finishedobject_id):
    """edit an existing finished object"""

    fo = get_object_or_404(FinishedObject, id=finishedobject_id)

    form = FinishedObjectForm(request.POST or None, instance=fo)
    form.helper.form_action = 'edit'
    if form.is_valid():
        form.save()

        return redirect('finishedobject_detail', finishedobject_id=fo.id)

    return render(request, 'backend/edit_finishedobject.html', {'form': form})


@login_required
def manufacturers(request):
    """show all manufacturers in db"""
    manufacturers = Manufacturer.objects.all()

    return render(request, 'backend/manufacturers.html', {'manufacturers':manufacturers})


@login_required
def add_manufacturer(request):
    """add a new manufacturer"""

    if request.method == 'POST':
        form = ManufacturerForm(request.POST)

        if form.is_valid():
            manufacturer = form.save()

            return redirect('manufacturers')

    else:
        form = ManufacturerForm()

    return render(request, 'backend/add_manufacturer.html', {'form': form}, )


@login_required
def add_manufacturer_modal(request):
    """add a new manufacturer when creating a new yarn"""
    form = ManufacturerForm()
    if request.method == 'POST':
        form = ManufacturerForm(request.POST)

        if form.is_valid():
            manufacturer = form.save()
            newname = bleach.clean(manufacturer.name)


            return JsonResponse({'name': newname,
                                 'id': manufacturer.id})
        else:

            return JsonResponse({'error': form.errors}, status=400)


    return render(request, 'backend/add_manufacturer_modal.html',
                  {'form': form}, )

@login_required
def add_yarnshop_collapse(request):
    """open yarnshop form in a collapsible"""
    form = YarnshopForm()
    if request.method == 'POST':
        form = YarnshopForm(request.POST)

        if form.is_valid():
            yarnshop = form.save()
            newname = bleach.clean(yarnshop.name)

            return JsonResponse({'name': newname,
                                 'id': yarnshop.id})
        else:
            return JsonResponse({'error': form.errors}, status=400)

    return render(request, 'backend/add_yarnshop_collapse.html',
                  {'form': form})


@login_required
def add_material_modal(request):
    """add a new material when creating a new yarn"""

    form = MaterialForm()
    if request.method == 'POST':
        form = MaterialForm(request.POST)

        if form.is_valid():
            material = form.save()
            newname = bleach.clean(material.name)


            return JsonResponse({'name': newname,
                                 'id': material.id})
        else:

            return JsonResponse({'error': form.errors}, status=400)

    return render(request, 'backend/add_material_modal.html',
                  {'form': form}, )


@login_required
def add_projectidea_modal(request):
    """add a missing projectidea when creating a new finished object"""

    form = ProjectideaForm2()


    if request.method == 'POST':
        form = ProjectideaForm2(request.POST)



        if form.is_valid():
            projectidea = form.save()
            newname = bleach.clean(projectidea.name)

            return JsonResponse({'name': newname, 'id': projectidea.id})

        else:

            return JsonResponse({'error': form.errors}, status=400)

    return render(request, 'backend/add_projectidea_modal.html',
                  {'form': form})



@login_required
def add_yarnshop_modal(request):
    """add a new yarnshop when creating a new color"""
    form = YarnshopForm()
    if request.method == 'POST':
        form = YarnshopForm(request.POST)

        if form.is_valid():
            yarnshop = form.save()
            newname = bleach.clean(yarnshop.name)

            return JsonResponse({'name': newname, 'id': yarnshop.id})

        else:

            return JsonResponse({'error': form.errors}, status=400)

    return render(request, 'backend/add_yarnshop_modal.html', {'form': form},)


@login_required
def add_yarn_modal(request):
    """add a yarn when creating a new projectidea"""
    form = YarnForm()

    if request.method == 'POST':
        form = YarnForm(request.POST)

        if form.is_valid():
            yarn = form.save()
            newname = bleach.clean(yarn.name)

            return JsonResponse({'name': newname, 'id': yarn.id})

        else:

            return JsonResponse({'error': form.errors}, status=400)

    return render(request, 'backend/add_yarn_modal.html', {'form': form})


@login_required
def add_color_modal(request):
    """add a color when creating a new projectidea"""

    form = ColorForm()
    if request.method == 'POST':
        form = ColorForm(request.POST)

        if form.is_valid():
            color = form.save()
            newname = bleach.clean(color.name)

            return JsonResponse({'name': newname, 'id': color.id})

        else:
            return JsonResponse({'error': form.errors}, status=400)

    return render(request, 'backend/add_color_modal.html', {'form': form})


@login_required
def delete_manufacturer(request, manufacturer_id):
    """delete selected manufacturer from db"""

    manufacturer = get_object_or_404(Manufacturer, pk=manufacturer_id)
    manufacturer.delete()

    messages.info(request, 'The manufacturer %s was successfully deleted' % manufacturer.name)

    return redirect('manufacturers')


@login_required
def yarnshops(request):
    """show all yarnshops"""

    yarnshops = Yarnshop.objects.all()

    return render(request, 'backend/yarnshops.html', {'yarnshops': yarnshops})


@login_required
def add_yarnshop(request):
    """add a new yarnshop"""

    if request.method == 'POST':
        form = YarnshopForm(request.POST)
        if form.is_valid():
            yarnshop = form.save()

            return redirect('yarnshops')

    else:
        form = YarnshopForm()

    return render(request, 'backend/add_yarnshop.html', {'form': form})


@login_required
def delete_yarnshop(request, yarnshop_id):
    """delete a specific yarnshop"""

    shop = get_object_or_404(Yarnshop, pk=yarnshop_id)
    shop.delete()
    messages.info(request, 'The yarnshop %s was successfully deleted' % shop.name)

    return redirect('yarnshops')


@login_required
def swatches(request):
    """show all swatches"""

    swatches = Swatch.objects.all()
    needlesizes = Needlesize.objects.all()
    yarns = Yarn.objects.all()

    return render(request, 'backend/swatches.html', {'swatches': swatches,
                                                     'needlesizes': needlesizes,
                                                     'yarns': yarns})

@login_required
def add_swatch(request):
    """add a swatch"""

    if request.method == 'POST':
        form = SwatchForm(request.POST)
        if form.is_valid():
            swatch = form.save()

            return redirect('swatches')

    else:
        form = SwatchForm()

    return render(request, 'backend/add_swatch.html', {'form': form})


@login_required
def delete_swatch(request, swatch_id):
    """delete swatch from db"""

    swatch = get_object_or_404(Swatch, pk=swatch_id)
    swatch.delete()
    messages.info(request, 'The swatch %s was successfully deleted' % swatch.name)

    return redirect('swatches')


@login_required
def materials(request):
    """show all materials"""

    materials = Material.objects.all()

    return render(request, 'backend/materials.html', {'materials': materials})


@login_required
def add_material(request):
    """ add a material"""
    if request.method == 'POST':
        form = MaterialForm(request.POST)
        if form.is_valid():
            material = form.save()

            return redirect('materials')

    else:
        form = MaterialForm()

    return render(request, 'backend/add_material.html', {'form': form})


@login_required
def delete_material(request, material_id):
    """delete material from db"""
    material = get_object_or_404(Material, pk=material_id)
    material.delete()
    messages.info(request, 'The material %s was successfully deleted' % material.name)

    return redirect('materials')


@login_required
def projectidea_to_finishedobject(request, projectidea_id):
    """take a projectidea and make a new finished object with the data"""

    projectidea = get_object_or_404(Projectidea, id=projectidea_id)
    fo = FinishedObject(name=projectidea.name, projectidea=projectidea, notes=projectidea.notes,
                        skeins_used=projectidea.skeins_needed, yarn=projectidea.yarn)

    form = FinishedObjectForm(instance=fo)
    if request.method == 'POST':
        form = FinishedObjectForm(request.POST, instance=fo)
        if form.is_valid():
            fo = form.save()
            return finishedobject_detail(request, finishedobject_id=fo.id)
        else:
            errors = form.errors.as_data()

            return render(request, 'backend/edit_finishedobject.html', {'form': form, 'errors': errors})
    else:

        return render(request, 'backend/edit_finishedobject.html', {'form': form})





