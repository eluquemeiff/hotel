from django.shortcuts import render
from .models import Chambre, Client
from .forms import MoveForm


def vue_hotel(request):
    chambres = Chambre.objects.all()
    form = MoveForm()
    return render(request, 'hotel/vue_hotel.html', {'chambres': chambres, 'form': form})


def client_detail(request, id):
    client = Client.objects.get(id_client=id)
    chambre = Chambre.objects.get(occupant=client)
    return render(request, 'hotel/detail_client.html', {'client': client, 'chambre': chambre})
