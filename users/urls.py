from django.urls import path
from . import views
from django.contrib.auth import views as auth_views  # Importă vizualizările standard pentru autentificare și deconectare

urlpatterns = [
    path('register/', views.register, name='register'),  # Înregistrare utilizator
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),  # Logare utilizator
    path('logout/', views.logout, name='logout'),  # Delogare utilizator
    path('', views.home, name='home'),
    path('locatari/', views.lista_locatari, name='lista_locatari'),
    path('apartamente/', views.lista_apartamente, name='lista_apartamente'),
    path('facturi/', views.lista_facturi, name='lista_facturi'),
    path('adauga_locatar/', views.adauga_locatar, name='adauga_locatar'),
    path('adauga_apartament/', views.adauga_apartament, name='adauga_apartament'),
    path('adauga_factura/', views.adauga_factura, name='adauga_factura'),
    path('facturi/sterge/<int:id>/', views.sterge_factura, name='sterge_factura'),
    path('locatar/sterge/<int:id>/', views.sterge_locatar, name='sterge_locatar'),
    path('apartament/sterge/<int:id>/', views.sterge_apartament, name='sterge_apartament'),
]
