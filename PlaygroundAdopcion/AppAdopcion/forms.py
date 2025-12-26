from django import forms
from AppAdopcion.models import Animal, Adoptante, Solicitud
from .models import Animal
from django.core.exceptions import ValidationError

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
    # Ceditar nombre y apellido del User 
    first_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    last_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Solicitud
        # Form para usuarios normales: NO incluimos 'estado'
        fields = ['telefono', 'mensaje']
        widgets = {
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Teléfono de contacto'}),
            'mensaje': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Mensaje (opcional)'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # hacemos telefono obligatorio 
        self.fields['telefono'].required = True

    def clean(self):
        cleaned = super().clean()
        first = (cleaned.get('first_name') or '').strip()
        last = (cleaned.get('last_name') or '').strip()
        telefono = (cleaned.get('telefono') or '').strip()

        # nombre, apellido y teléfono obligatorios
        if not first:
            self.add_error('first_name', 'El nombre es obligatorio.')
        if not last:
            self.add_error('last_name', 'El apellido es obligatorio.')
        if not telefono:
            self.add_error('telefono', 'El teléfono es obligatorio.')

        if self.errors:
            raise ValidationError("Por favor corrige los errores en el formulario.")

        return cleaned


class SolicitudAdminForm(forms.ModelForm):
    # campo 'estado' visible para admins
    first_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    last_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Solicitud
        fields = ['telefono', 'mensaje', 'estado']
        widgets = {
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Teléfono de contacto'}),
            'mensaje': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Mensaje (opcional)'}),
            'estado': forms.Select(attrs={'class': 'form-select'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['telefono'].required = True

    def clean(self):
        cleaned = super().clean()
        first = (cleaned.get('first_name') or '').strip()
        last = (cleaned.get('last_name') or '').strip()
        telefono = (cleaned.get('telefono') or '').strip()

        if not first:
            self.add_error('first_name', 'El nombre es obligatorio.')
        if not last:
            self.add_error('last_name', 'El apellido es obligatorio.')
        if not telefono:
            self.add_error('telefono', 'El teléfono es obligatorio.')

        if self.errors:
            raise ValidationError("Por favor corrige los errores en el formulario.")

        return cleaned
