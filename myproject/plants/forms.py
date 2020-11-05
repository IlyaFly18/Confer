from django import forms
from .models import Plant


class PlantFrom(forms.ModelForm):

    class Meta:
        model = Plant
        fields = ['name', 'desc']
        labels = {
            'name': 'Название',
            'desc': 'Описание',
        }