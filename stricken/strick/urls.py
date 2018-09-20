from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('yarns', views.yarns, name='yarns'),
    path('projectideas', views.projectideas, name='projectideas'),
    path('yarns/<yarntype_id>', views.yarntype, name='yarntype')
]

