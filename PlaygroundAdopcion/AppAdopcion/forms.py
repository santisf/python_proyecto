from django import forms
from AppAdopcion.models import Animal, Adoptante, Solicitud

class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ['nombre', 'especie', 'edad', 'descripcion']

class AdoptanteForm(forms.ModelForm):
    class Meta:
        model = Adoptante
        fields = ['nombre', 'apellido', 'email', 'telefono']

class SolicitudForm(forms.ModelForm):
    class Meta:
        model = Solicitud
        fields = ['animal_nombre', 'adoptante_nombre', 'fecha_de_solicitud', 'estado']