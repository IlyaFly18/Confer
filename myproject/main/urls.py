from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('accounts/', include('accounts.urls')),
    path('beds/', include('beds.urls')),
    path('ground/', include('weather.urls')),
    path('notif/', include('notif.urls')),

    path('send_developer_message', views.send_developer_message, name='send_developer_message'),
]