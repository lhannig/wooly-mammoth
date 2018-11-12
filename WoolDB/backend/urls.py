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
    path('yarns/add/manufacturer', views.add_manufacturer_modal, name='add_manufacturer_modal'),


    # Colors
    path('yarns/<int:yarntype_id>/colors/<int:color_id>',
         views.color_detail,
         name='color_detail'),
    path('yarns/<int:yarntype_id>/colors/add', views.add_color,
         name='add_color'),
    path('yarns/<int:yarntype_id>/colors/<int:color_id>/edit',
         views.edit_color, name='edit_color'),
    path('yarns/<int:yarntype_id>/colors/<int:color_id>/delete',
         views.delete_color, name='delete_color'),


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
    path('ajax/load-colors/', views.load_colors, name='ajax_load_colors'),
    path('projectideas/<int:projectidea_id>/finished', views.projectidea_to_finishedobject,
         name='projectidea_to_finishedobject'),

    # finished objects
    path('finishedobjects', views.finishedobjects, name='finishedobjects'),
    path('finishedobjects/add', views.add_fo, name='add_fo'),
    path('finishedobjects/<int:finishedobject_id>',
         views.finishedobject_detail, name='finishedobject_detail'),
    path('finishedobjects/<int:finishedobject_id>/delete',
         views.delete_finishedobject, name='delete_finishedobject'),
    path('finishedobjects/<int:finishedobject_id>/edit',
         views.edit_fo, name='edit_finishedobject'),

    # manufacturers
    path('manufacturers', views.manufacturers, name='manufacturers'),
    path('manufacturers/add', views.add_manufacturer, name='add_manufacturer'),
    path('manufacturers/<int:manufacturer_id>/delete', views.delete_manufacturer, name='delete_manufacturer'),



    # yarnshops
    path('yarnshops', views.yarnshops, name='yarnshops'),
    path('yarnshops/add', views.add_yarnshop, name='add_yarnshop'),
    path('yarnshops/<int:yarnshop_id>/delete', views.delete_yarnshop, name='delete_yarnshop'),

    # swatches
    path('swatches', views.swatches, name='swatches'),
    path('swatches/add', views.add_swatch, name='add_swatch'),
    path('swatches/<int:swatch_id>/delete', views.delete_swatch, name='delete_swatch'),

    # materials
    path('materials', views.materials, name='materials'),
    path('materials/add', views.add_material, name='add_material'),
    path('materials/<int:material_id>/delete', views.delete_material, name='delete_material'),


                ]

