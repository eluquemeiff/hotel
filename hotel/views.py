from django.shortcuts import render
from .models import Chambre, Client



def vue_hotel(request):
    chambres = Chambre.objects.all()
    return render(request, 'hotel/vue_hotel.html', {'chambres': chambres})

def client_detail (request, id):
    client=Client.objects.get(id_client=id)
    chambre=Chambre.objects.get(occupant=client)
    return render(request, 'hotel/detail_client.html',{'client':client,'chambre':chambre})