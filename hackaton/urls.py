from django.contrib import admin
from django.urls import path, include
from django_registration.backends.one_step.views import RegistrationView
from accounts.forms import RegisterForm
from index.views import IndexView
from quest import urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/register/',
        RegistrationView.as_view(
            form_class=RegisterForm, success_url='/'
        ),
        name='registration_register'),
    path('accounts/', include('django_registration.backends.one_step.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('quest/', include('quest.urls')),
    path('', IndexView.as_view(), name='index'),

]
