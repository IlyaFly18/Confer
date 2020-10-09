from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path('', views.index, name = "index"),
    path('accounts/', include('accounts.urls')),
    path('ground/', include('weather.urls')),
]