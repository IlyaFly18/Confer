from django import forms
from .models import Bed

class BedForm(forms.ModelForm):
    name = forms.CharField(label='Название объекта',  max_length=30, min_length=5)
    shape = forms.ChoiceField(choices=(
        ('1', 'Прямоугольная'),
        ('2', 'Круглая')), label='Форма'
    )
    class Meta:
        model = Bed
        fields = ('name', 'shape')

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if len(name) < 5:
            raise forms.ValidationError('Имя должно быть длиной больше либо равно 5 символам')
        return name
