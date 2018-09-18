from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from itertools import islice, chain
from .models import Yarn, Manufacturer, Material, Needlesize, Color

# Create your views here.

def index(request):
    template = loader.get_template('strick/index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def yarns(request):
    context = {}
    yarns = Yarn.objects.filter(color__own_it = True).distinct()
    materials = Material.objects.all()

    materials = Material.objects.all()
    colors = Color.objects.all()






    return render(request, 'strick/yarns.html',
                   {'yarns': yarns, 'materials': materials, 'colors': colors,})


