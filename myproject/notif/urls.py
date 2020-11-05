from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path('', views.index, name='notif_index'),
    path('notif_done', views.notif_done, name='notif_done'),
]
