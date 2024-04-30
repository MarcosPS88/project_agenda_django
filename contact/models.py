from typing import Any
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f'{self.name}'

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
    category = models.ForeignKey(Category, 
                                 on_delete=models.SET_NULL, #on_delete = diz o que fazer com contact se category 
                                 blank=True,        # for deletado. Está configurado para setar NULL caso 
                                 null=True)      #category deletado. Importante o campo estar blank e permitir null
    owner = models.ForeignKey(User,
                              on_delete=models.SET_NULL,
                              blank=True,
                              null=True)                  

    def __str__(self) -> str:          # Metodo implementado para trocar o nome de exibição
        return f'{self.first_name} {self.last_name}'  # No Admin do Django

