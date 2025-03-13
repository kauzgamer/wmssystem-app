from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class UserProfile(models.Model):
    """Modelo para armazenar informações adicionais de usuários."""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    foto = models.ImageField(upload_to='profile_pics', blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    cargo = models.CharField(max_length=100, blank=True, null=True)
    departamento = models.CharField(max_length=100, blank=True, null=True)
    data_nascimento = models.DateField(blank=True, null=True)
    data_contratacao = models.DateField(default=timezone.now)
    cpf = models.CharField(max_length=14, blank=True, null=True)
    observacoes = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f'Perfil de {self.user.username}'