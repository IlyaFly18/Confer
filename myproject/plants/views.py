from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseNotFound
from beds.models import Bed
from .models import Plant, PlantFunction
from .forms import PlantFrom

import datetime

def bed_valid(request):
    listurls = list(request.path.split('/'))
    indBed = listurls.index('bed')
    bed_id = listurls[indBed + 1]
    bed = Bed.objects.get(id=bed_id, user=request.user)
    return bed


@login_required
def bed_plants(request):
    if bed_valid(request):
        bed = bed_valid(request)
        form = PlantFrom()
        plants = Plant.objects.filter(bed=bed)
        context = {
            'bed': bed,
            'form': form,
            'plants': plants,
        }
        return render(request, 'plants/index.html', context)
    else:
        return HttpResponseNotFound('Страница не найдена')

@login_required
@csrf_exempt
def plant_create(request):
    name = request.POST['name']
    desc = request.POST['desc']
    x = request.POST['x']
    y = request.POST['y']
    day = request.POST['day']
    month = request.POST['month']
    year = request.POST['year']
    date = datetime.date(day=int(day), month=int(month), year=int(year))
    if bed_valid(request):
        bed = bed_valid(request)
        plant = Plant(name=name, desc=desc, bed=bed, x=x, y=y, date=date)
        plant.save()
        plants = Plant.objects.filter(bed=bed)
        context = {
            'plants': plants,
        }
        return render(request, 'plants/index.html', context)
    else:
        return HttpResponseNotFound('Страница не найдена')


@login_required
@csrf_exempt
def plant_get(request):
    today = datetime.date.today()
    plant_id = request.POST['id']
    plant = Plant.objects.get(id=plant_id)
    if plant:
        functions = PlantFunction.objects.filter(plant=plant_id).order_by('first_date')
        for function in functions:
            if function.first_date < today:
                function.first_date = today
                function.save()
        context = {
            'plant': plant,
            'functions': functions,
            'functions_size': len(functions),
        }
        return render(request, 'plants/plants-info.html', context)
    else:
        return HttpResponseNotFound('Растение не найдено')

@login_required
@csrf_exempt
def plant_save(request):
    name = request.POST['name']
    desc = request.POST['desc']
    id = request.POST['id']
    plant = Plant.objects.get(id=id)
    plant.name = name
    plant.desc = desc
    plant.save()
    context = {
        'plant': plant,
    }
    return render(request, 'plants/plants-info.html', context)

@login_required
@csrf_exempt
def plant_del(request):
    id = request.POST['id']
    plant = Plant.objects.get(id=id)
    bed = plant.bed
    plant.delete()
    plants = Plant.objects.filter(bed=bed)
    context = {
        'plants': plants,
    }
    return render(request, 'plants/index.html', context)


@login_required
@csrf_exempt
def function_create(request):
    name = request.POST['name']
    first_date = request.POST['first_date']
    period = request.POST['period']
    day = request.POST['day']
    month = request.POST['month']
    year = request.POST['year']
    first_date = first_date.split('-')
    first_date = datetime.date(day=int(first_date[2]), month=int(first_date[1]), year=int(first_date[0]))
    today = datetime.date(day=int(day), month=int(month), year=int(year))
    plant = Plant.objects.get(id=request.POST['plant_id'])
    function = PlantFunction(name=name, first_date=first_date, period=period, plant=plant)
    if function.first_date < today:
        function.first_date = today
    function.save()
    functions = PlantFunction.objects.filter(plant=request.POST['plant_id']).order_by('first_date')
    context = {
        'functions_size': len(functions),
        'functions': functions,
    }
    return render(request, 'plants/plants-info.html', context)


@login_required
@csrf_exempt
def function_del(request):
    id = request.POST['id']
    plant_id = request.POST['plant_id']
    function = PlantFunction.objects.get(id=id)
    function.delete()
    functions = PlantFunction.objects.filter(plant=plant_id).order_by('first_date')
    context = {
        'functions': functions,
        'functions_size': len(functions),
    }
    return render(request, 'plants/plants-info.html', context)



