from typing import Any
from django.db import models
from django.utils import timezone

# Create your models here.

class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100, blank=True) # Blank para não ser obrigatório
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=254, blank=True)
    created_date = models.DateTimeField(default=timezone.now) # Função para gerar data automatica
    description = models.TextField(blank=True)
    show = models.BooleanField(default=True)
    picture = models.ImageField(blank=True, upload_to='pictures/%Y/%m/' ) # Indicando pasta e dizendo para criar
                                                                     # pasta /pictures/ano/mes  dentro de /media

    def __str__(self) -> str:          # Metodo implementado para trocar o nome de exibição
        return f'{self.first_name} {self.last_name}'  # No Admin do Django
