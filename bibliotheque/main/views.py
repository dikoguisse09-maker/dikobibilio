from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Auteur
from .forms import AuteurForm, livreForm
from django.contrib.auth import authenticate,login,logout


def connexion(request):
    erreur = ""
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            erreur="Nom d'utilisateur ou mot de passe incorrect"
    return render(request, "login.html", {'erreur': erreur})


def deconnexion(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def home(request):
    person=Auteur.objects.all()
    return render(request, 'index.html', {'person': person})


@login_required(login_url='login')
def ajouter_auteur(request):
    if request.method == 'POST':
        form = AuteurForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  
    else:
        form = AuteurForm()
    return render(request, 'ajouter_auteur.html', {'form': form})


@login_required(login_url='login')
def ajouter_livre(request):
    if request.method == 'POST':
        form = livreForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')  # ✅ redirect au lieu de render
    else:
        form = livreForm()
    return render(request, 'ajouter_livre.html', {'form': form})


@login_required(login_url='login')
def modifier_auteur(request, id):           # ✅ prend un id en paramètre
    auteur = get_object_or_404(Auteur, id=id)
    form = AuteurForm(request.POST or None, instance=auteur)  # ✅ charge l'auteur existant
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'modifier_auteur.html', {'form': form})


def about(request):
    return render(request, 'about.html')