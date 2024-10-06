from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import Locatar, Apartament, Factura
from .forms import LocatarForm, ApartamentForm, FacturaForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required  # Pentru a obliga autentificarea
from django.shortcuts import render, redirect, get_object_or_404
@login_required  # Obligă utilizatorii să fie autentificați pentru a accesa pagina home
def home(request):
    return render(request, 'users/home.html')

def home(request):
    return render(request, 'users/home.html')

def lista_locatari(request):
    locatari = Locatar.objects.all()
    return render(request, 'users/lista_locatari.html', {'locatari': locatari})

def lista_apartamente(request):
    apartamente = Apartament.objects.all()
    return render(request, 'users/lista_apartamente.html', {'apartamente': apartamente})

def lista_facturi(request):
    facturi = Factura.objects.all()
    return render(request, 'users/lista_facturi.html', {'facturi': facturi})

def adauga_locatar(request):
    if request.method == 'POST':
        form = LocatarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_locatari')
    else:
        form = LocatarForm()
    return render(request, 'users/adauga_locatar.html', {'form': form})

def adauga_apartament(request):
    if request.method == 'POST':
        form = ApartamentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_apartamente')
    else:
        form = ApartamentForm()
    return render(request, 'users/adauga_apartament.html', {'form': form})

def adauga_factura(request):
    if request.method == 'POST':
        form = FacturaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_facturi')
    else:
        form = FacturaForm()
    return render(request, 'users/adauga_factura.html', {'form': form})

# Funcția pentru înregistrare utilizator
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserRegistrationForm

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Setează parola criptată
            user.save()
            login(request, user)  # Autentifică utilizatorul după înregistrare
            return redirect('home')  # Redirecționează către pagina principală după autentificare
    else:
        form = UserRegistrationForm()  # Afișează formularul gol pentru GET request
    return render(request, 'users/register.html', {'form': form})

def sterge_locatar(request, id):
    locatar = get_object_or_404(Locatar, id=id)
    locatar.delete()
    return redirect('lista_locatari')

def sterge_apartament(request, id):
    apartament = get_object_or_404(Apartament, id=id)
    apartament.delete()
    return redirect('lista_apartamente')

def sterge_factura(request, id):
    factura = get_object_or_404(Factura, id=id)
    factura.delete()
    return redirect('lista_facturi')
def logout(request):
    return render(request, 'users/logout.html')
