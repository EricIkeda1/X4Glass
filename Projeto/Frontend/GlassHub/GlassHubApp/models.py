from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)  
    nome = models.CharField(max_length=100) 
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions '
                  'granted to each of their groups.'
    )
    
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',  
        blank=True,
        help_text='Specific permissions for this user.'
    )

    USERNAME_FIELD = 'email' 
    REQUIRED_FIELDS = ['username', 'nome']
    
class eventos(models.Model):
    name = models.CharField(max_length=100)       # Nome do evento
    width = models.IntegerField()                 # Largura do evento
    height = models.IntegerField()                # Altura do evento
    code = models.CharField(max_length=50)        # Código do evento
    order_id = models.IntegerField()              # ID do pedido relacionado
    created_at = models.DateTimeField(auto_now_add=True)  # Adiciona a data e hora do evento automaticamente

    def __str__(self):
        return f"{self.name} (Order ID: {self.order_id})"
    
