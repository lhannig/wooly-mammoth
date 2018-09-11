from django.contrib import admin

# Register your models here.
from .models import Yarn, FinishedObject, Swatch, Projectideas, Wash, Weight

admin.site.register(Yarn)
admin.site.register(FinishedObject)
admin.site.register(Swatch)
admin.site.register(Projectideas)
admin.site.register(Wash)
admin.site.register(Weight)