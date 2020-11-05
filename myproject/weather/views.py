from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
import json
from .models import RainPeriod
import requests
# Create your views here.

@csrf_exempt
@login_required
def index(request):
    context = {
        'active_url': request.path.split('/')[1],
    }
    """if request.method == "POST":
        data = request.POST['data']
        data = json.loads(data)
        obj = RainPeriod(city= data['name'], description_weather=)"""
    return render(request, 'weather/index.html', context)
