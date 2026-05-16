from django import forms
from .models import Auteur, livre

class AuteurForm(forms.ModelForm):
    
    class Meta:
        model = Auteur
        fields = ['nom', 'prenom', 'nationalite']  
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom de l\'auteur'}),
            'prenom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Prénom de l\'auteur'}),
            'nationalite': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nationalité de l\'auteur'}),  # ✅
        }

class livreForm(forms.ModelForm):
    class Meta:
        model = livre
        fields = ['titre', 'auteur', 'isbn', 'annee', 'disponible', 'couverture']
        widgets = {
            'titre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titre du livre'}),
            'auteur': forms.Select(attrs={'class': 'form-control'}),
            'isbn': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ISBN'}),
            'annee': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Année de publication'}),
            'disponible': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'couverture': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }