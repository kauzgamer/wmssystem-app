from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from desktop.models.user_models import UserProfile

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """Cria um perfil de usuário quando um novo usuário é criado."""
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """Salva o perfil do usuário quando o usuário é atualizado."""
    try:
        instance.profile.save()
    except UserProfile.DoesNotExist:
        UserProfile.objects.create(user=instance)