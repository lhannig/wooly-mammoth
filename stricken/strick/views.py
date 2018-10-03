from django.shortcuts import render, get_object_or_404, redirect
from django.core.exceptions import ValidationError
from django.http import Http404
from django.http import HttpResponse
from django.template import loader
from itertools import islice, chain
from .models import Yarn, Manufacturer, Material, Needlesize, Color,\
    Projectidea, Weight
from .forms import YarnForm, ColorForm

# Create your views here.

def index(request):
    '''returns index site'''
    template = loader.get_template('strick/index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def yarns(request):
    '''shows all yarns in stash'''

    yarns = Yarn.objects.filter(color__own_it = True).distinct()

    materials = Material.objects.all()
    colors = Color.objects.all()

    return render(request, 'strick/yarns.html',
                   {'yarns': yarns, 'materials': materials,
                    'colors': colors,})


def yarn_detail(request, yarntype_id):
    '''shows one single yarn type and its proberties'''

    colors = Color.objects.filter(yarntype=yarntype_id).filter(own_it=True)
    yarn = Yarn.objects.get(pk=yarntype_id)

    return render(request, 'strick/yarn_detail.html', {'colors': colors, 'yarn':yarn,})


def color_detail(request, yarntype_id, color_id):
    '''shows one color of a specific yarn'''
    color = Color.objects.filter(yarntype_id=yarntype_id).get(pk=color_id)

    return render(request, 'strick/color.html', {'color': color,})


def add_yarn(request):
    '''add a new yarn type'''

    if request.method == 'POST':
        form = YarnForm(request.POST)
        if form.is_valid():
            yarn = form.save()

            return redirect('yarn_detail', yarntype_id=yarn.pk)

    else:
        form = YarnForm()

    return render(request, 'strick/add_yarn.html', {'form': form,})


def add_color(request, yarntype_id):
    '''add a new color for an existing yarn type'''

    if request.method == 'POST':
        form = ColorForm(request.POST)
        if form.is_valid():

            color = form.save(commit=False)
            color.yarntype = yarntype_id

            color.save()

            return redirect('color_detail', yarntype_id=yarntype_id, color_id=color.pk)

    else:
        form = ColorForm()

    return render(request, 'strick/add_color.html', {'form': form,})


def edit_yarn(request, yarntype_id):
    '''edit an existing yarn type'''

    instance = get_object_or_404(Yarn, id=yarntype_id)
    form = YarnForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('yarn_detail', yarntype_id=instance.id)
    return render(request, 'strick/edit_yarn.html', {'form': form,})


def edit_color(request, color_id):
    '''edit an existing color'''

    instance = get_object_or_404(Color, id=color_id)
    yarntype_id = Yarn.objects.get(color=instance.id).id

    form = ColorForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('color_detail', yarntype_id=yarntype_id, color_id=instance.id)
    return render(request, 'strick/edit_color.html', {'form': form,})


def projectideas(request):
    '''show all existing projectideas'''

    projectideas = Projectidea.objects.all()
    yarns = Yarn.objects.all()
    colors = Color.objects.all()
    weights = Weight.objects.all()

    return render(request, 'strick/projectideas.html',
                  {'projectideas': projectideas, 'yarns': yarns,
                   'colors': colors, 'weights': weights,})