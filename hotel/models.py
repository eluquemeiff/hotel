from django.db import models


class Chambre(models.Model):
    id_chambre = models.IntegerField(max_length=100, primary_key=True)
    occupant = models.ForeignKey("Client", on_delete=models.CASCADE, null=True, blank=True)
    couleur=models.CharField(max_length=100)
    propre=models.BooleanField()
    photo = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return str(self.id_chambre)

class Client(models.Model):
    id_client = models.IntegerField(max_length=100, primary_key=True)
    nom = models.CharField(max_length=20)
    prenom = models.CharField(max_length=20)
    couleur_pref = models.CharField(max_length=20)
    photo = models.CharField(max_length=200, null=True, blank=True)
    nb_nuit = models.IntegerField()
    def __str__(self):
        return f"{self.prenom} {self.nom}"

