from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="index"),
    path('about', views.about, name="about"),
    path('ajouter_auteur', views.ajouter_auteur, name="ajouter_auteur"),        
    path('ajouter_livre', views.ajouter_livre, name="ajouter_livre"),           
    path('modifier_auteur/<int:id>/' , views.modifier_auteur, name="modifier_auteur"),  
    path('login', views.connexion, name="login"),
    path('logout' , views.deconnexion, name="deconnexion"),
]
