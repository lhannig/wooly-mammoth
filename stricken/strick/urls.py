from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('yarns', views.yarns, name='yarns'),
    path('projectideas', views.projectideas, name='projectideas'),
    path('yarns/<int:yarntype_id>', views.show_one_yarntype, name='yarntype'),
    path('yarns/<int:yarntype_id>/<int:color_id>', views.show_color, name='show_color'),
    path('yarns/new_yarn', views.new_yarn, name='new_yarn')
]

