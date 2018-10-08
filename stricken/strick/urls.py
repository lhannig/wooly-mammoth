from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    # Yarns
    path('yarns', views.yarns, name='yarns'),

    path('yarns/<int:yarntype_id>',
         views.yarn_detail, name='yarn_detail'),

    path('yarns/<int:yarntype_id>/edit', views.edit_yarn,
         name='edit_yarn'),

    path('yarns/add', views.add_yarn, name='add_yarn'),

    path('yarns/<int:yarntype_id>/delete', views.delete_yarn,
         name='delete_yarn'),


    # Colors
    path('yarns/<int:yarntype_id>/colors/<int:color_id>',
         views.color_detail,
         name='color_detail'),
    path('yarns/<int:yarntype_id>/colors/add', views.add_color,
         name='add_color'),
    path('yarns/<int:yarntype_id>/colors/<int:color_id>/edit',
         views.edit_color, name='edit_color'),

    # Projectideas
    path('projectideas', views.projectideas, name='projectideas'),
    path('projectideas/add', views.add_projectidea,
         name='add_projectidea'),
    path('projectideas/<int:projectidea_id>',
         views.projectidea_detail,
         name='projectidea_detail'),
    path('projectideas/<int:projectidea_id>/edit',
         views.edit_projectidea,
         name='edit_projectidea'),
    path('projectideas/<int:projectidea_id>/delete',
         views.delete_projectidea, name='delete_projectidea'),

                ]

