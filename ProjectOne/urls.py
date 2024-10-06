from django.contrib import admin
from django.urls import path, include
from users.views import home  # Importăm vizualizarea home
from django.contrib.auth import views as auth_views  # Importăm vizualizarea de logare

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from users.views import home  # Importă vizualizarea home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),  # Include URL-urile pentru aplicația "users"
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),  # Pagină de logare
    path('', home, name='home'),  # Pagină principală cu meniu
]
