from django import forms

from .models import Cliente
class ClienteModelForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = [
            'nome',
            'cognome',
            'cf',
        ]