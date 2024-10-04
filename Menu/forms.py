from django import forms
from .models import Menu, Plato

class FormMenu(forms.ModelForm):
    fecha = forms.DateField(
        widget=forms.DateInput(
            format='%Y-%m-%d',
            attrs={
                'type': 'date',
                'class': 'form-control',
            }
        )
    )

    class Meta:
        model = Menu
        fields = ['fecha']


class FormPlato(forms.ModelForm):
    class Meta:
        model = Plato
        fields = ['nombre', 'tipo']
