from django.shortcuts import render
from .models import Auteur
from .forms import AuteurForm


# Create your views here.


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



