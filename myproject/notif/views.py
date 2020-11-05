from django.shortcuts import render
from plants.models import PlantFunction, Plant
from beds.models import Bed
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from jinja2 import Template
import datetime



def render_context(request, today):
    notif = {
        'today': list(),
        'tomorrow': list(),
    }
    delta = datetime.timedelta(days=1)
    tomorrow = today+delta
    beds = Bed.objects.filter(user=request.user)
    for bed in beds:
        plants = Plant.objects.filter(bed=bed.id)
        for plant in plants:
            functions = PlantFunction.objects.filter(plant=plant.id)
            for func in functions:
                if func.first_date < today:
                    func.first_date = today
                    func.save()
                if func.first_date == today:
                    notif['today'].append({
                        'bed': bed,
                        'plant': plant,
                        'func': func,
                    })
                elif func.first_date == tomorrow:
                    notif['tomorrow'].append({
                        'bed': bed,
                        'plant': plant,
                        'func': func,
                    })
    context = {
        'active_url': request.path.split('/')[1],
        'notif': notif,
    }
    return context

@csrf_exempt
@login_required
def index(request):
    if request.method == 'POST':
        day = request.POST['day']
        month = request.POST['month']
        year = request.POST['year']
        today = datetime.date(day=int(day), month=int(month), year=int(year))
        context = render_context(request, today)
        return render(request, 'notif/index.html', context)
    return render(request, 'notif/index.html', {})


@login_required
@csrf_exempt
def notif_done(request):
    id = request.POST['id']
    day = request.POST['day']
    month = request.POST['month']
    year = request.POST['year']
    today = datetime.date(day=int(day), month=int(month), year=int(year))
    function = PlantFunction.objects.get(id=id)
    if function.period == 0:
        function.delete()
    else:
        delta = datetime.timedelta(days=function.period)
        function.first_date += delta
        function.save()
    context = render_context(request, today)
    return render(request, 'notif/index.html', context)
