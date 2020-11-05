from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path('', views.index, name="beds_index"),
    path('bed_del', views.bed_del, name="beds_delete"),
    path('bed_create', views.bed_create, name="beds_create"),

    path('plants/', include('plants.urls'))
]