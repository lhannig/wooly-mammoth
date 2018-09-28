from django.shortcuts import render, get_object_or_404, redirect
from django.core.exceptions import ValidationError
from django.http import Http404
from django.http import HttpResponse
from django.template import loader
from itertools import islice, chain
from .models import Yarn, Manufacturer, Material, Needlesize, Color, Projectidea
from .forms import YarnForm

# Create your views here.

def index(request):
    template = loader.get_template('strick/index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def yarns(request):

    yarns = Yarn.objects.filter(color__own_it = True).distinct()
    materials = Material.objects.all()

    materials = Material.objects.all()
    colors = Color.objects.all()

    return render(request, 'strick/yarns.html',
                   {'yarns': yarns, 'materials': materials, 'colors': colors,})


def projectideas(request):
    projectideas = Projectidea.objects.all()

    return render(request, 'strick/projectideas.html', {'projectideas': projectideas,})


def show_one_yarntype(request, yarntype_id):
    colors = Color.objects.filter(yarntype=yarntype_id).filter(own_it=True)
    yarn = Yarn.objects.get(pk=yarntype_id)

    return render(request, 'strick/yarntype.html', {'colors': colors, 'yarn': yarn,})


def show_color(request, yarntype_id, color_id):
    color = Color.objects.filter(yarntype_id=yarntype_id).get(pk=color_id)

    return render(request, 'strick/color.html', {'color': color,})


def new_yarn(request):

    if request.method == 'POST':
        form = YarnForm(request.POST)
        if form.is_valid():
            yarn = form.save()

            return redirect('yarn_detail', yarntype_id=yarn.pk)

    else:
        form = YarnForm()

    return render(request, 'strick/new_yarn.html', {'form': form,})

