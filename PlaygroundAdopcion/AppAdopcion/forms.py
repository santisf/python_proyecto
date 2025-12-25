from django import forms
from AppAdopcion.models import Animal, Adoptante, Solicitud
from .models import Animal

class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ['nombre', 'especie', 'edad', 'descripcion', 'estado', 'foto']


class AdoptanteForm(forms.ModelForm):
    class Meta:
        model = Adoptante
        fields = ['nombre', 'apellido', 'email', 'telefono']

"""class SolicitudForm(forms.ModelForm):
    class Meta:
        model = Solicitud
        fields = ['animal', 'adoptante', 'fecha_de_solicitud', 'estado']"""



class SolicitudForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, required=False, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=30, required=False, widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = Solicitud
        fields = ['telefono', 'mensaje', 'estado']
        widgets = {
            'telefono': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Teléfono de contacto'}),
            'mensaje': forms.Textarea(attrs={'class':'form-control', 'rows':3, 'placeholder':'Mensaje (opcional)'}),
            'estado': forms.Select(attrs={'class':'form-select'}),
        }
