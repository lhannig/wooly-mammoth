from django.contrib import admin

# Register your models here.
from .models import Yarn, FinishedObject, Swatch, Projectideas

admin.site.register(Yarn)
admin.site.register(FinishedObject)
admin.site.register(Swatch)
admin.site.register(Projectideas)