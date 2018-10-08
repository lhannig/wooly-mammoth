from itertools import islice, chain

from django.shortcuts import render, get_object_or_404, redirect
from django.core.exceptions import ValidationError
from django.http import Http404
from django.http import HttpResponse
from django.template import loader
from django.contrib import messages

from strick.models import Yarn, Manufacturer, Material, Needlesize, Color, \
                          Projectidea, Weight
from strick.forms import YarnForm, ColorForm, ProjectideaForm

# Create your views here.

def index(request):
    """returns index site"""
    return render(request, 'strick/index.html')
    # template = loader.get_template('strick/index.html')
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

    return render(request, 'strick/yarns.html', {
        'yarns': yarns,
        'materials': materials,
        'colors': colors,
        'unstashed_yarns': unstashed_yarns,
    })


def yarn_detail(request, yarntype_id):
    """shows one single yarn type and its proberties"""
    colors = Color.objects.filter(yarntype=yarntype_id, own_it=True)
    yarn = Yarn.objects.get(pk=yarntype_id)

    return render(request, 'strick/yarn_detail.html', {
        'colors': colors,
        'yarn':yarn,
    })


def delete_yarn(request, yarn_id):
    """ delete a yarntype from the database """

    yarn = get_object_or_404(Yarn, pk=yarn_id)
    yarn.delete()

    return render(request, 'strick/confirmation.html')


def color_detail(request, yarntype_id, color_id):
    """shows one color of a specific yarn"""
    color = Color.objects.filter(yarntype_id=yarntype_id).get(pk=color_id)

    return render(request, 'strick/color.html', {'color': color,})


def add_yarn(request):
    """Add a new yarn"""
    if request.method != "POST":
        return render(request, 'strick/add_yarn.html', {
            'form': YarnForm()
        })

    form = YarnForm(request.POST)
    if form.is_valid():
        yarn = form.save()

        return redirect('yarn_detail', yarntype_id=yarn.pk)

    return render(request, 'strick/add_yarn.html', {
        'form': form,
    })


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

    return render(request, 'strick/add_color.html', {'form': form, })


def edit_yarn(request, yarntype_id):
    """edit an existing yarn type"""
    yarn = get_object_or_404(Yarn, id=yarntype_id)
    form = YarnForm(request.POST or None, instance=yarn)
    if form.is_valid():
        form.save()

        return redirect('yarn_detail', yarntype_id=yarn.id)

    return render(request, 'strick/edit_yarn.html', {'form': form, })


def edit_color(request, yarntype_id, color_id):
    """edit an existing color"""

    instance = get_object_or_404(Color, pk=color_id)
    form = ColorForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance.own_it = instance.quantity > 0
        form.save()

        return redirect('color_detail',
                        yarntype_id=yarntype_id,
                        color_id=instance.id)

    return render(request, 'strick/edit_color.html', {'form': form, })


def projectideas(request):
    """show all existing projectideas"""
    projectideas = Projectidea.objects.all()
    yarns = Yarn.objects.all()
    colors = Color.objects.all()
    weights = Weight.objects.all()

    return render(request, 'strick/projectideas.html', {
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

            return redirect ('projectidea_detail',
                             projectidea_id=projectidea.pk)

    else:
        form = ProjectideaForm()

    return render(request, 'strick/add_projectidea.html', {'form': form},)


def projectidea_detail(request, projectidea_id):
    """display one projectidea"""
    projectidea = get_object_or_404(Projectidea, pk=projectidea_id)
    colors = Color.objects.filter(projectidea__id=projectidea_id)

    return render(request, 'strick/projectidea_detail.html', {
        'projectidea': projectidea,
        'colors': colors,
    })


def delete_projectidea(request, projectidea_id):
    """remove a projectidea from db"""
    project = get_object_or_404(Projectidea, pk=projectidea_id)
    project.delete()

    return render(request, 'strick/confirmation.html')


def edit_projectidea(request, projectidea_id):
    """edit an existing projectidea"""
  #  projectidea_id = request.POST.get('projectidea_id')
    instance = get_object_or_404(Projectidea, id=projectidea_id)

    form = ProjectideaForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()

        return redirect('projectidea_detail', projectidea_id=instance.id)

    return render(request, 'strick/edit_projectidea.html', {'form': form})



