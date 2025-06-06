# Create your models here.

from django.contrib.auth.models import AbstractUser
from django.db import models

class UsuarioIF(AbstractUser):
    matricula = models.CharField(max_length=20, unique=True)
    nome_completo = models.CharField(max_length=150)

    def __str__(self):
        return self.username


