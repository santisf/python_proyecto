
# Create your models here.

from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    telefono = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return f"{self.user.username} - Profile"

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    else:
        Profile.objects.get_or_create(user=instance)


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
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    telefono = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Solicitud(models.Model):
    ESTADOS = [
        ("en_proceso", "En proceso"),
        ("aprobado", "Aprobado"),
        ("cancelado", "Cancelado"),
    ]

    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    adoptante = models.ForeignKey(Adoptante, on_delete=models.CASCADE)
    fecha_de_solicitud = models.DateField()
    estado = models.CharField(
        max_length=20,
        choices=ESTADOS,
        default="en_proceso"
    )

    def __str__(self):
        return f"Solicitud de {self.adoptante} para {self.animal} ({self.get_estado_display()})"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Actualizar estado del animal según la solicitud
        if self.estado == "aprobado":
            self.animal.estado = "adoptado"
        else:
            # Si no está aprobado, el animal sigue disponible
            self.animal.estado = "disponible"
        self.animal.save()