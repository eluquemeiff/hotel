from django import forms
from .models import Chambre


class MoveForm(forms.ModelForm):
    class Meta:
        model = Chambre
        fields = ('id_chambre',)