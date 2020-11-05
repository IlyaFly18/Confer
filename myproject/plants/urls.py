from django.urls import path, re_path, include
from . import views

urlpatterns = [
    # path('', views.index, name='plants_index'),

    re_path(r'^bed/\d+/$', views.bed_plants, name='plants_index'),

    re_path(r'^bed/\d+/plant_create$', views.plant_create, name='plant_create'),
    re_path(r'^bed/\d+/plant_get$', views.plant_get, name='plant_get'),
    re_path(r'^bed/\d+/plant_save$', views.plant_save, name='plant_save'),
    re_path(r'^bed/\d+/plant_del$', views.plant_del, name='plant_del'),

    re_path(r'^bed/\d+/function_create$', views.function_create, name='function_create'),
    re_path(r'^bed/\d+/function_del$', views.function_del, name='function_del'),
]
