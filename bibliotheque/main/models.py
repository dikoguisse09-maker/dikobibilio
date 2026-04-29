from django.db import models

class Auteur(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    nationalite = models.CharField(max_length=50)

   
class Livre(models.Model):

    titre = models.CharField(max_length=200)
    auteur = models.ForeignKey(Auteur, on_delete=models.CASCADE)
    isbn = models.CharField(max_length=13, unique=True)
    annee = models.IntegerField()
    disponible = models.BooleanField(default=True)
    couverture = models.ImageField(upload_to='covers/', blank=True)

    def __str__(self):
        return self.titre