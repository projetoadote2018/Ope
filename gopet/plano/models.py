from django.db import models

# Create your models here.
class Planos (models.Model):
    nome_plano = models.CharField(max_length=25)
    preco = models.DecimalField(max_digits=9, decimal_places=2, name='Preço')
    status = models.CharField(max_length=10, name='Nome')
    descricao = models.CharField(name='Descrição', max_length=100)
    forma_pagamento = models.CharField(name='Forma de pagamento', max_length=20)
    def __str__(self):
        return self.nome
