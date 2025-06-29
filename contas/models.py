from django.db import models
from django.contrib.auth.models import User

TIPO_USUARIO_CHOICES = (
    ('discente', 'Discente'),
    ('docente', 'Docente'),
    ('outro', 'Outro'),
)

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    numero = models.CharField(max_length=20, blank=True)
    foto = models.ImageField(upload_to='fotos_perfil/', blank=True, null=True)
    curso = models.CharField(max_length=100, blank=True)
    tipo_usuario = models.CharField(max_length=20, choices=TIPO_USUARIO_CHOICES, default='discente')

    def __str__(self):
        return f"Perfil de {self.user.username}"

# Signals para criar e salvar perfil automaticamente

from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def criar_perfil(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(user=instance)

@receiver(post_save, sender=User)
def salvar_perfil(sender, instance, **kwargs):
    # Evitar erro caso usuário não tenha perfil (exemplo, em teste)
    if hasattr(instance, 'perfil'):
        instance.perfil.save()
