from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('about',views.about),
    path('ajouter_auteur',views.ajouter_auteur,name="ajouter"),
    path('modifier_auteur',views.modifier_auteur,name="modifier_auteur"),
]