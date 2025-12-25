
# Create your models here.

from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone



class Animal(models.Model):
    ESTADOS = [
        ("disponible", "Disponible"),
        ("adoptado", "Adoptado"),
    ]

    nombre = models.CharField(max_length=40)
    especie = models.CharField(max_length=40)
    edad = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=200, blank=True)
    estado = models.CharField(
        max_length=20,
        choices=ESTADOS,
        default="disponible"
    )
    #Foto del animal
    foto = models.ImageField(upload_to="media/animales/", blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} ({self.get_estado_display()})"

class Adoptante(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=30, blank=True, null=True)
    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Solicitud(models.Model):
    ESTADOS = [
        ("en_proceso", "En proceso"),
        ("aprobado", "Aprobado"),
        ("cancelado", "Cancelado"),
    ]

    animal = models.ForeignKey('Animal', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=30, blank=True, null=True)
    mensaje = models.TextField(blank=True)
    fecha_de_solicitud = models.DateField(default=timezone.now)
    estado = models.CharField(max_length=20, choices=ESTADOS, default="en_proceso")

    def __str__(self):
        nombre_usuario = self.user.get_full_name() or self.user.username
        return f"Solicitud de {nombre_usuario} para {self.animal} ({self.get_estado_display()})"

    def save(self, *args, **kwargs):
        # detectar cambio de estado para actualizar fecha
        if self.pk:
            old = Solicitud.objects.filter(pk=self.pk).first()
            old_estado = old.estado if old else None
        else:
            old_estado = None

        # si es nueva o cambió el estado, actualizar fecha a hoy
        if old_estado is None or old_estado != self.estado:
            self.fecha_de_solicitud = timezone.now().date()

        super().save(*args, **kwargs)

        # actualizar estado del animal según la solicitud
        if self.estado == "aprobado":
            self.animal.estado = "adoptado"
        else:
            # si no está aprobado, dejar disponible (ajustá si querés otra lógica)
            self.animal.estado = "disponible"
        self.animal.save()


