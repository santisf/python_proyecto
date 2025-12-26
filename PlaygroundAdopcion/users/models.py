
from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()

class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares/', null=True, blank=True)

    def __str__(self):
        # si no hay imagen devuelve username
        if self.imagen:
            return f"{settings.MEDIA_URL}{self.imagen}"
        return f"Avatar de {self.user.username}"

# Señal para crear avatar
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def crear_avatar_al_crear_usuario(sender, instance, created, **kwargs):
    if created:
        Avatar.objects.create(user=instance)
    else:
        # asegurar que exista la instancia vatar para usuarios existentes
        Avatar.objects.get_or_create(user=instance)
