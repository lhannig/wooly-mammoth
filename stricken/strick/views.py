from django.shortcuts import render
from django.http import HttpResponse
from .models import Yarn

# Create your views here.

def index(request):
    return HttpResponse('Wolldatenbank')

def yarns(request):
    yarns = Yarn.objects.all()
    output = ', '.join([y.name for y in yarns])
    return HttpResponse(output)
