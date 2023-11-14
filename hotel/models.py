from django.db import models
from random import randint


class Chambre(models.Model):
    id_chambre = models.IntegerField(primary_key=True)
    occupant = models.ForeignKey("Client", on_delete=models.CASCADE, null=True, blank=True)
    couleur=models.CharField(max_length=100)
    propre=models.BooleanField()
    photo = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return str(self.id_chambre)

class Client(models.Model):
    id_client = models.IntegerField(primary_key=True)
    nom = models.CharField(max_length=20)
    prenom = models.CharField(max_length=20)
    couleur_pref = models.CharField(max_length=20)
    chambre_occupee = models.ForeignKey("Chambre", on_delete=models.CASCADE, null=True, blank=True)
    photo = models.CharField(max_length=200, null=True, blank=True)
    nb_nuit = models.IntegerField()
    def __str__(self):
        return f"{self.prenom} {self.nom}"

    @classmethod
    def newClient(cls):
        noms_de_famille = [
            "Smith", "Johnson", "Williams", "Jones", "Brown",
            "Davis", "Miller", "Wilson", "Moore", "Taylor",
            "Anderson", "Thomas", "Jackson", "White", "Harris",
            "Martin", "Thompson", "Garcia", "Martinez", "Robinson",
            "Clark", "Rodriguez", "Lewis", "Lee", "Walker",
            "Hall", "Allen", "Young", "Hernandez", "King",
            "Wright", "Lopez", "Hill", "Scott", "Green",
            "Adams", "Baker", "Nelson", "Carter", "Mitchell",
            "Perez", "Roberts", "Turner", "Phillips", "Campbell",
            "Parker", "Evans", "Edwards", "Collins", "Stewart"
        ]
        prenoms = [
            "John", "Jane", "Robert", "Emily", "Michael",
            "Emma", "David", "Olivia", "Christopher", "Sophia",
            "Matthew", "Ava", "Andrew", "Isabella", "Daniel",
            "Mia", "William", "Abigail", "Ethan", "Ella",
            "Joseph", "Madison", "James", "Liam", "Benjamin",
            "Grace", "Logan", "Harper", "Ryan", "Aiden",
            "Oliver", "Avery", "Jack", "Scarlett", "Alexander",
            "Chloe", "Henry", "Sofia", "Sebastian", "Evelyn",
            "Samuel", "Victoria", "Nathan", "Lily", "Daniel",
            "Hannah", "Nicholas", "Aria", "Caleb", "Grace"
        ]
        couleurs = ["jaune", "bleu", "vert", "rouge"]
        nom = noms_de_famille[randint(0, 49)]
        prenom = prenoms[randint(0, 49)]
        couleur = couleurs[randint(0, 3)]
        nbNuit = randint(1, 10)
        id = Client.objects.aggregate(max_attribut=models.Max('id_client'))['max_attribut']  # nouveau id = 1+ max ancien client
        if id == None:
            id = 0
        id += 1

        return Client.objects.create(id_client=id,
                                          nom=nom,
                                          prenom=prenom,
                                          couleur_pref=couleur,
                                          nb_nuit=nbNuit)