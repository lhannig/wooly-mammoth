from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.http import HttpResponse
from django.template import loader
from itertools import islice, chain
from .models import Yarn, Manufacturer, Material, Needlesize, Color, Projectidea
from .forms import RenewNrinStash

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

    if request.method == 'GET':

        cols = Color.objects.filter(yarntype=yarntype_id).filter(own_it=True)
        return render(request, 'strick/yarntype.html', {'cols': cols,})



    if request.method == 'POST':

        color = Color.objects.get(pk=request.POST['col_id'])
        new_nr_form = RenewNrinStash(request.POST, instance=color)

        new_nr_form.save()

        cols = Color.objects.filter(yarntype=yarntype_id).filter(own_it=True)
        return render(request, 'strick/yarntype.html', {'cols': cols, })





