from django.shortcuts import render
from .models import Chambre


def vue_hotel(request):
    chambres = Chambre.objects.all()
    return render(request, 'hotel/vue_hotel.html', {'chambres': chambres})