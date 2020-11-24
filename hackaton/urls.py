from django.contrib import admin
from django.urls import path, include
from django_registration.backends.one_step.views import RegistrationView
from accounts.forms import RegisterForm
from index.views import IndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/register/',
        RegistrationView.as_view(
            form_class=RegisterForm, success_url='/'
        ),
        name='registration_register'),
    path('accounts/', include('django_registration.backends.one_step.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', IndexView.as_view(), name='index'),

]
