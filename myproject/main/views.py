from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.conf import settings

def index(request):
    context = {
        'active_url': request.path.split('/')[1]
    }
    return render(request, "main/index.html", context)


@csrf_exempt
def send_developer_message(request):
    topic = request.POST['topic']
    body = request.POST['body']
    user = request.user
    send_mail(topic+"  (user="+str(user.id)+")", body, settings.EMAIL_HOST_USER, ['idaleshin@mail.ru'])
    return render(request, "main/index.html", {})


