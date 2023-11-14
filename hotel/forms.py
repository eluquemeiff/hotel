from django import forms
from .models import Client


class MoveForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('chambre_occupee',)  # on affecte une chambre au client pommé


class PasseNuitForm(forms.Form):  # on fait un forme qui n'a aucun champ
    pass

class NettoyerForm(forms.Form):
    pass
