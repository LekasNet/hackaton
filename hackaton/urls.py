from django.contrib import admin
from django.urls import path, include
<<<<<<< HEAD
from django_registration.backends.one_step.views import RegistrationView
from accounts.forms import RegisterForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/register/',
        RegistrationView.as_view(
            form_class=RegisterForm
        ),
        name='registration_register'),
    path('accounts/', include('django_registration.backends.one_step.urls')),
    path('accounts/', include('django.contrib.auth.urls')),

=======


urlpatterns = [
    path('admin/', admin.site.urls),
    path('quests/', include('quests.urls'))
>>>>>>> 1c9da7500892db88db646a35ce7cc9b29f6cd366
]
