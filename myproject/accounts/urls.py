from django.urls import path, re_path, include
from . import views
from django.contrib.auth.views import LogoutView, LoginView
from django.contrib.auth import views as auth_views
from .forms import SetPasswordForm, PasswordResetForm

urlpatterns = [
    re_path(r'^sign_up$', views.signup, name="signup"),

    #Подтверждение почты
    path('sign_up/conf_email', views.confEmail, name="conf_email"),
    path('sign_up/conf_email/success', views.sucConfEmail, name="sucConfEmail"),

    #Вход и Выход
    path('login', LoginView.as_view(template_name='accounts/login.html'), name="login"),
    path('logout', LogoutView.as_view(), {'next_page': 'settings.LOGOUT_REDIRECT_URL'}, name='logout'),

    #Reset password
    path('password_reset', auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html', form_class = PasswordResetForm, email_template_name = 'accounts/reset_password_email.html'), name="password_reset", ),
    path('password_reset_done', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'), name="password_reset_done"),
    path('password_reset_confirm/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html', form_class=SetPasswordForm), name='password_reset_confirm'),
    path('password_reset_complete', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'), name='password_reset_complete'),
]