from django import forms
from .models import ActividadDeportiva


class ActividadDeportivaForm(forms.ModelForm):
    class Meta:
        model = ActividadDeportiva
        fields = ['nombre', 'descripcion', 'lugar', 'cupo']
        widgets = {'descripcion': forms.Textarea(attrs={'rows': 4})}

    def clean_cupo(self):
        cupo = self.cleaned_data['cupo']
        if cupo < 1:
            raise forms.ValidationError('El cupo debe ser al menos 1.')
        return cupo
