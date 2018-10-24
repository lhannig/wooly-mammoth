from itertools import islice, chain

from django.shortcuts import render, get_object_or_404, redirect
from django.core.exceptions import ValidationError
from django.http import Http404
from django.http import HttpResponse
from django.template import loader
from django.contrib import messages
from django.forms import formset_factory

from Backend.models import Yarn, Manufacturer, Material, Needlesize, Color, \
                          Projectidea, Weight, FinishedObject, Yarnshop, Swatch
from Backend.forms import YarnForm, ColorForm, ProjectideaForm, FinishedObjectForm, ManufacturerForm,\
                        YarnshopForm, SwatchForm, MaterialForm

# Create your views here.

def index(request):
    """returns index site"""
    return render(request, 'Backend/index.html')
    # template = loader.get_template('Backend/index.html')
    # context = {}
    # return HttpResponse(template.render(context, request))


def yarns(request):
    """shows all yarns in stash and yarns currently unstashed """

    yarns = Yarn.objects.filter(color__own_it=True).distinct() \
                        .order_by('manufacturer__name', 'name')

    unstashed_yarns = Yarn.objects.exclude(color__own_it=True).distinct() \
                                  .order_by('manufacturer__name', 'name')

    materials = Material.objects.all()
    colors = Color.objects.all()

    return render(request, 'Backend/yarns.html', {
        'yarns': yarns,
        'materials': materials,
        'colors': colors,
        'unstashed_yarns': unstashed_yarns,
    })


def yarn_detail(request, yarntype_id):
    """shows one single yarn type and its proberties"""
    colors = Color.objects.filter(yarntype=yarntype_id, own_it=True)
    yarn = Yarn.objects.get(pk=yarntype_id)

    return render(request, 'Backend/yarn_detail.html', {
        'colors': colors,
        'yarn':yarn,
    })


def delete_yarn(request, yarntype_id):
    """delete a yarntype from the database and all of its colors"""

    yarn = get_object_or_404(Yarn, pk=yarntype_id)
    yarn.delete()
    messages.info(request, 'The yarn %s was successfully deleted' %yarn.name)

    return redirect('yarns')

def add_yarn(request):
    """Add a new yarn"""
    if request.method != "POST":
        return render(request, 'Backend/add_yarn.html', {
            'form': YarnForm()
        })

    form = YarnForm(request.POST)
    if form.is_valid():
        yarn = form.save()

        return redirect('yarn_detail', yarntype_id=yarn.pk)

    return render(request, 'Backend/add_yarn.html', {
        'form': form,
    })


def edit_yarn(request, yarntype_id):
    """edit an existing yarn type"""
    yarn = get_object_or_404(Yarn, id=yarntype_id)
    form = YarnForm(request.POST or None, instance=yarn)
    if form.is_valid():
        form.save()

        return redirect('yarn_detail', yarntype_id=yarn.id)

    return render(request, 'Backend/edit_yarn.html', {'form': form, })

def color_detail(request, yarntype_id, color_id):
    """shows one color of a specific yarn"""
    color = Color.objects.filter(yarntype_id=yarntype_id).get(pk=color_id)

    return render(request, 'Backend/color.html', {'color': color,})



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

    return render(request, 'Backend/add_color.html', {'form': form, })



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

    return render(request, 'Backend/edit_color.html', {'form': form, })

def delete_color(request, yarntype_id, color_id):
    """ delete a color from the db """
    color = get_object_or_404(Color, pk=color_id)
    color.delete()
    messages.info(request,
                  'The color %s was successfully deleted' % color.color)

    return redirect('yarn_detail', yarntype_id)


def projectideas(request):
    """show all existing projectideas"""
    projectideas = Projectidea.objects.all()
    yarns = Yarn.objects.all()
    colors = Color.objects.all()
    weights = Weight.objects.all()

    return render(request, 'Backend/projectideas.html', {
        'projectideas': projectideas,
        'yarns': yarns,
        'colors': colors,
        'weights': weights,
    })


def add_projectidea(request):
    """add a new idea for a project"""

    if request.method == 'POST':
        form = ProjectideaForm(request.POST)
        if form.is_valid():
            projectidea = form.save()

            return redirect('projectidea_detail',
                             projectidea_id=projectidea.pk)

    else:
        form = ProjectideaForm()

    return render(request, 'Backend/add_projectidea.html', {'form': form},)


def load_colors(request):
    """load colors depending on yarnchoice"""
    yarn_id = request.GET.get('yarn')
    colors = Color.objects.filter(yarntype=yarn_id).order_by('color')

    return render(request, 'Backend/dropdownlist_colors.html',
                  {'colors': colors,})


def projectidea_detail(request, projectidea_id):
    """display one projectidea"""
    projectidea = get_object_or_404(Projectidea, pk=projectidea_id)
    colors = Color.objects.filter(projectidea__id=projectidea_id)

    return render(request, 'Backend/projectidea_detail.html', {
        'projectidea': projectidea,
        'colors': colors,
    })


def delete_projectidea(request, projectidea_id):
    """remove a projectidea from db"""
    project = get_object_or_404(Projectidea, pk=projectidea_id)
    project.delete()
    messages.info(request,
                  'The projectidea %s was successfully deleted' % project.name)

    return redirect('projectideas')


def edit_projectidea(request, projectidea_id):
    """edit an existing projectidea"""
  #  projectidea_id = request.POST.get('projectidea_id')
    instance = get_object_or_404(Projectidea, id=projectidea_id)

    form = ProjectideaForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()

        return redirect('projectidea_detail', projectidea_id=instance.id)

    return render(request, 'Backend/edit_projectidea.html', {'form': form})


def finishedobjects(request):
    """show all finished objects"""
    finishedobjects = FinishedObject.objects.all()
    yarns = Yarn.objects.all()
    needlesizes = Needlesize.objects.all()
    colors = Color.objects.all()

    return render(request, 'Backend/finishedobjects.html',
                  {'finishedobjects': finishedobjects, 'yarns':yarns,
                            'needlesizes': needlesizes, 'colors':colors},)

def add_fo(request):
    """add a finished object"""

    if request.method == 'POST':
        form = FinishedObjectForm(request.POST)
        if form.is_valid():
            finishedobject = form.save()

            return redirect('finishedobject_detail',
                            finishedobject_id=finishedobject.pk)

    else:
        form = FinishedObjectForm()

    return render(request, 'Backend/add_finishedobject.html', {'form': form}, )


def finishedobject_detail(request, finishedobject_id):
    """shows details of a selected finished object"""

    finishedobject = FinishedObject.objects.get(pk=finishedobject_id)
    colors = Color.objects.all()
    needlesizes = Needlesize.objects.all()

    return render(request, 'Backend/finishedobject_detail.html',
                  {'finishedobject': finishedobject, 'colors': colors,
                   'needlesizes': needlesizes},)

def delete_finishedobject(request, finishedobject_id):
    """delete a finished object"""

    fo = get_object_or_404(FinishedObject, pk=finishedobject_id)
    fo.delete()
    messages.info(request, 'The finished object %s was successfully deleted' % fo.name)

    return redirect('finishedobjects')


def edit_fo(request, finishedobject_id):
    """edit an existing finished object"""

    fo = get_object_or_404(FinishedObject, id=finishedobject_id)

    form = FinishedObjectForm(request.POST or None, instance=fo)
    if form.is_valid():
        form.save()

        return redirect('finishedobject_detail', finishedobject_id=fo.id)

    return render(request, 'Backend/edit_finishedobject.html', {'form': form})


def manufacturers(request):
    """show all manufacturers in db"""
    manufacturers = Manufacturer.objects.all()

    return render(request, 'Backend/manufacturers.html', {'manufacturers':manufacturers})


def add_manufacturer(request):
    """add a new manufacturer"""

    if request.method == 'POST':
        form = ManufacturerForm(request.POST)
        if form.is_valid():
            manufacturer = form.save()

            return redirect('manufacturers')

    else:
        form = ManufacturerForm()

    return render(request, 'Backend/add_manufacturer.html', {'form': form}, )

def delete_manufacturer(request, manufacturer_id):
    """delete selected manufacturer from db"""

    manufacturer = get_object_or_404(Manufacturer, pk=manufacturer_id)
    manufacturer.delete()

    messages.info(request, 'The manufacturer %s was successfully deleted' % manufacturer.name)

    return redirect('manufacturers')


def yarnshops(request):
    """show all yarnshops"""

    yarnshops = Yarnshop.objects.all()

    return render(request, 'Backend/yarnshops.html', {'yarnshops': yarnshops})


def add_yarnshop(request):
    """add a new yarnshop"""

    if request.method == 'POST':
        form = YarnshopForm(request.POST)
        if form.is_valid():
            yarnshop = form.save()

            return redirect('yarnshops')

    else:
        form = YarnshopForm()

    return render(request, 'Backend/add_yarnshop.html', {'form': form})


def delete_yarnshop(request, yarnshop_id):
    """delete a specific yarnshop"""

    shop = get_object_or_404(Yarnshop, pk=yarnshop_id)
    shop.delete()
    messages.info(request, 'The yarnshop %s was successfully deleted' % shop.name)

    return redirect('yarnshops')


def swatches(request):
    """show all swatches"""

    swatches = Swatch.objects.all()

    return render(request, 'Backend/swatches.html', {'swatches': swatches})

def add_swatch(request):
    """add a swatch"""

    if request.method == 'POST':
        form = SwatchForm(request.POSt)
        if form.is_valid():
            swatch = form.save()

            return redirect('swatches')

    else:
        form = SwatchForm()

    return render(request, 'Backend/add_swatch.html', {'form': form})


def delete_swatch(request, swatch_id):
    """delete swatch from db"""

    swatch = get_object_or_404(Swatch, pk=swatch_id)
    swatch.delete()
    messages.info(request, 'The swatch %s was successfully deleted' % swatch.name)

    return redirect('swatches')


def materials(request):
    """show all materials"""

    materials = Material.objects.all()

    return render(request, 'Backend/materials.html', {'materials': materials})

def add_material(request):
    """ add a material"""
    if request.method == 'POST':
        form = MaterialForm(request.POST)
        if form.is_valid():
            material = form.save()

            return redirect('materials')

    else:
        form = MaterialForm()

    return render(request, 'Backend/add_material.html', {'form': form})


def delete_material(request, material_id):
    """delete material from db"""
    material = get_object_or_404(Material, pk=material_id)
    material.delete()
    messages.info(request, 'The material %s was successfully deleted' % material.name)

    return redirect('materials')


def projectidea_to_finishedobject(request, projectidea_id):
    """take a projectidea and make a new finished object with the data"""

    projectidea = get_object_or_404(Projectidea, id=projectidea_id)
    fo = FinishedObject(name='Choose a name', projectidea=projectidea, notes=projectidea.notes,
                        skeins_used=projectidea.skeins_needed, yarn=projectidea.yarn)

    fo.save()


    form = FinishedObjectForm(instance=fo)
    if form.is_valid():
        form.save()

        return redirect('finishedobject_detail', finishedobject_id=fo.id)

    return render(request, 'Backend/edit_finishedobject.html', {'form': form})



