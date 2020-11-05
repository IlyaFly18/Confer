from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseNotFound
import json

from .models import Bed
from .forms import BedForm




@login_required
def index(request):
    # if request.method == 'POST':
    #     form = BedForm(request.POST)
    #     print('POST in index')
    #     if form.is_valid():
    #         bed = form.save(commit=False)
    #         bed.user = request.user
    #         bed.shape = dict(bed.SHAPE_CHOICES).get(bed.shape)
    #         bed.save()
    #         beds = Bed.objects.all()
    #         context = {
    #             'beds': beds,
    #         }
    #         return redirect('beds_index')
    #     else:
    #         form.add_error(None, 'Форма не прошла валидацию')
    form = BedForm()

    beds = Bed.objects.filter(user=request.user).order_by('-id')
    context = {
        'form': form,
        'beds': beds,
        'size': len(beds),
        'active_url': request.path.split('/')[1],
    }
    return render(request, "beds/index.html", context)

@csrf_exempt
def bed_del(request):
    bed_id = request.POST['bed_id']
    try:
        bed = Bed.objects.get(id= bed_id)
        bed.delete()
        beds = Bed.objects.filter(user=request.user).order_by('-id')
        context = {
            'beds': beds,
            'size': len(beds),
        }
        return render(request, "beds/beds_list.html", context)
    except:
        return HttpResponseNotFound("<h2>Грядка не найдена</h2>")

@csrf_exempt
def bed_create(request):
    bed_name = request.POST['name']
    bed_shape = request.POST['shape']
    bed = Bed(name=bed_name, user=request.user)
    bed.shape = dict(bed.SHAPE_CHOICES).get(bed_shape)
    bed.save()
    beds = Bed.objects.filter(user=request.user).order_by('-id')
    context = {
        'beds': beds,
        'size': len(beds),
    }
    return render(request, "beds/beds_list.html", context)


