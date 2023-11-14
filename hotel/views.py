from django.shortcuts import render, get_object_or_404, redirect
from .models import Chambre, Client
from .forms import *
from random import randint
from django.db import models


def vue_hotel(request):
    if request.method == "POST":
        if "move" in request.POST:
            client = get_object_or_404(Client, chambre_occupee=None)  # on prend le client à la réception
            form = MoveForm(request.POST, instance=client)  # s'il y a qqch dans la requête POST on met ça dans le formulaire et on va l'appliquer au client à la réception

            if form.is_valid():  # si le formulaire tient la route, alors on traite le contenu
                form.save(commit=False)  # on update le client dans le Python mais pas dans la db
                chambre = get_object_or_404(Chambre, id_chambre=client.chambre_occupee.id_chambre)
                if (chambre.occupant is None) and chambre.propre and (client.couleur_pref == chambre.couleur):
                    chambre.occupant = client
                    client.save()
                    chambre.save()

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
                    nom = noms_de_famille[randint(0,49)]
                    prenom = prenoms[randint(0,49)]
                    couleur = couleurs[randint(0,3)]
                    nbNuit = randint(1,10)
                    id = Client.objects.aggregate(max_attribut=models.Max('id_client'))['max_attribut'] + 1  #  nouveau id = 1+ max ancien client
                    newClient = Client.objects.create(id_client=id,
                                                      nom=nom,
                                                      prenom=prenom,
                                                      couleur_pref=couleur,
                                                      nb_nuit=nbNuit)
                    newClient.save()

        elif "passeNuit" in request.POST:
            if PasseNuitForm(request.POST).is_valid():
                clients = Client.objects.all()
                for client in clients:
                    if client.chambre_occupee is not None:
                        client.nb_nuit -= 1
                        if client.nb_nuit <= 0:
                            chambre = client.chambre_occupee
                            client.delete()
                            chambre.occupant = None
                            chambre.propre = False
                            chambre.save()
                        else:
                            client.save()

        elif "nettoyer" in request.POST:
            if NettoyerForm(request.POST).is_valid():
                chambre = get_object_or_404(Chambre, id_chambre=request.POST.get("nettoyer"))
                chambre.propre = True
                chambre.save()


    moveForm = MoveForm()
    passeNuitForm = PasseNuitForm()
    nettoyerForm = NettoyerForm()
    chambres = Chambre.objects.all()
    client = get_object_or_404(Client, chambre_occupee=None)

    return render(request, 'hotel/vue_hotel.html', {'chambres': chambres,
                                                    'moveForm': moveForm,
                                                    'passeNuitForm': passeNuitForm,
                                                    'nettoyerForm': nettoyerForm,
                                                    'client': client,
                                                    })


def client_detail(request, id):
    client = Client.objects.get(id_client=id)
    chambre = Chambre.objects.get(occupant=client)
    return render(request, 'hotel/detail_client.html', {'client': client, 'chambre': chambre})
