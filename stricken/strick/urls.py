from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('yarns', views.yarns, name='yarns'),
    path('projectideas', views.projectideas, name='projectideas'),
    path('yarns/<int:yarntype_id>/<int:color_id>', views.color_detail, name='color_detail'),
    path('yarns/add_yarn', views.add_yarn, name='add_yarn'),
    path('yarns/<int:yarntype_id>', views.yarn_detail, name='yarn_detail'),
    path('yarns/add_color', views.add_color, name='add_color')

]

