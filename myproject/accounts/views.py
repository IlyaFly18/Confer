from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
from django.conf import settings

import random

from .forms import SignUpForm, ConfEmail
from django.contrib.auth.decorators import login_required

def generate_code():
    random.seed()
    return str(random.randint(100000, 999999))

def signup(request):
    if request.user.is_authenticated:
        return redirect("index")
    else:
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                new_user = form.save(commit=False)
                new_user.set_password(form.cleaned_data['password'])
                new_user.save()
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    confemail = user
                    confemail.confEmail = False
                    confemail.save()
                    message = generate_code()
                    email = request.user.email
                    code = request.user
                    code.emailcode = int(message)
                    code.save()
                    send_mail(
                        'Код подтверждения',
                        message,
                        settings.EMAIL_HOST_USER,
                        [email],
                        fail_silently=False,
                    )
                    return redirect(request.path + '/conf_email')
                else:
                    form.add_error(None, 'Unknown or disabled account')
                return redirect("index")
            else:
                #form.add_error(None, 'Invalid syntax')
                return render(request, 'accounts/signup.html', {'form': form})

        else:
            form = SignUpForm()
            return render(request, 'accounts/signup.html', {'form': form})

def confEmail(request):
    if request.user.is_authenticated:
        if (request.method == 'POST'):
            form = ConfEmail(request.POST)
            if form.is_valid():
                code = form.cleaned_data.get('code')
                if (request.user.emailcode == str(code)):
                    user = request.user
                    user.confEmail = True
                    user.save()
                    send_mail(
                        'Подтверждение почты',
                        'Ваша почта успешно подтверждена!\n'+'Gard&Gard приветствует Вас!',
                        settings.EMAIL_HOST_USER,
                        [request.user.email],
                        fail_silently=False,
                    )
                    return redirect('sucConfEmail')
                else:
                    form.add_error(None, "Неверный код!")
        else:
            form = ConfEmail()
        return render(request, 'accounts/confemail.html', {'form': form})
    else:
        return redirect('index')


def sucConfEmail(request):
    return render(request, 'accounts/succonfemail.html', {})

