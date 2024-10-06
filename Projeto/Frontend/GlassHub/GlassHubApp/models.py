from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)  # E-mail deve ser único
    nome = models.CharField(max_length=100)  # Campo para nome

    # Adicione related_name para evitar conflitos
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # Mude aqui
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions '
                  'granted to each of their groups.'
    )
    
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',  # Mude aqui
        blank=True,
        help_text='Specific permissions for this user.'
    )

    USERNAME_FIELD = 'email'  # Usar e-mail como campo de autenticação
    REQUIRED_FIELDS = ['username', 'nome']