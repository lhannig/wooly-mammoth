from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Yarn

# Create your views here.

def index(request):
    template = loader.get_template('strick/index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def yarns(request):
    yarns = Yarn.objects.all()
    output = ', '.join([y.name for y in yarns])
    return HttpResponse(output)
