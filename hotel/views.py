from django.shortcuts import render
from .models import Chambre, Client
from .forms import *


def vue_hotel(request):
    try:
        client = Client.objects.get(chambre_occupee=None)  # on prend le client à la réception
    except:
        client = Client.newClient()

    if request.method == "POST":
        if "move" in request.POST:
            form = MoveForm(request.POST,
                            instance=client)  # s'il y a qqch dans la requête POST on met ça dans le formulaire et on va l'appliquer au client à la réception

            if form.is_valid():  # si le formulaire tient la route, alors on traite le contenu
                form.save(commit=False)  # on update le client dans le Python mais pas dans la db
                if client.chambre_occupee:
                    chambre = Chambre.objects.get(id_chambre=client.chambre_occupee.id_chambre)
                    if (chambre.occupant is None) and chambre.propre and (client.couleur_pref == chambre.couleur):
                        chambre.occupant = client
                        client.save()
                        chambre.save()
                        Client.newClient().save()  # utilisation de la fonction de classe de la classe Client dans le fichier models.py

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
                    else:
                        client.delete()
                        Client.newClient().save()

        elif "nettoyer" in request.POST:
            if NettoyerForm(request.POST).is_valid():
                chambre = Chambre.objects.get(id_chambre=request.POST.get("nettoyer"))
                chambre.propre = True
                chambre.save()

    moveform = MoveForm()
    passenuitform = PasseNuitForm()
    nettoyerform = NettoyerForm()
    chambres = Chambre.objects.all()

    return render(request, 'hotel/vue_hotel.html', {'chambres': chambres,
                                                    'moveform': moveform,
                                                    'passeNuitForm': passenuitform,
                                                    'nettoyerForm': nettoyerform,
                                                    'client': client,
                                                    })


def client_detail(request, id):
    client = Client.objects.get(id_client=id)
    chambre = Chambre.objects.get(occupant=client)
    return render(request, 'hotel/detail_client.html', {'client': client, 'chambre': chambre})
