from django.contrib import admin

# Register your models here.
from .models import Yarn, FinishedObject, Swatch,  Wash, Weight, Manufacturer, Material, Yarnshop, Color, Projectidea, Needlesize

admin.site.register(Yarn)
admin.site.register(FinishedObject)
admin.site.register(Swatch)
admin.site.register(Projectidea)
admin.site.register(Wash)
admin.site.register(Weight)
admin.site.register(Manufacturer)
admin.site.register(Material)
admin.site.register(Yarnshop)
admin.site.register(Color)
admin.site.register(Needlesize)