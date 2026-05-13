from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Auteur
from .forms import AuteurForm, livreForm
from django.contrib.auth import authenticate,login,logout

# Create your views here.


def connexion(request):
    erreur=""

    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")

        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('index')
        
        else:
            erreur="Nom d'utilisateur ou mot de passe incorrect"

    return render(request,"login.html",{'erreur':erreur})




@login_required(login_url='login')
def home(request):
    person=Auteur.objects.all()
    context={
        'person':person
    }
    return render(request,'index.html',context) 

def ajouter_auteur(request):
    if request.method == 'POST':
        form = AuteurForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'index.html')
    else:
        form = form = AuteurForm()
    
    context = {
        'form': form
    }
    return render(request, 'ajouter_auteur.html', context)


def ajouter_livre(request):
    if request.method == 'POST':
        form = livreForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return render(request,'index.html')
    else:
        form = form = livreForm()
    
    context = {
        'form': form
    }
    return render(request, 'ajouter_livre.html', context)



def about(request):
    return render(request, 'about.html')

def modifier_auteur(request):
    if request.method == 'POST':
        form = AuteurForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'index.html')
    else:
        form = form = AuteurForm()
    
    context = {
        'form': form
    }
    return render(request, 'modifier_auteur.html', context)

def deconnexion(request):
    logout(request)
    return redirect ('login')

