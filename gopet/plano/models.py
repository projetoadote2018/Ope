from django.db import models

# Create your models here.
class Planos (models.Model):
    nome = models.Charfield(max_length=25)
    preco = models.DecimalField(max_digits=9, decimal_places=2, name='Preço')
    status = models.Charfield(max_length=10, name='Nome')
    descricao = models.TextArea(name='Descrição')
    forma_pagamento = models.Charfield(name='Forma de pagamento')
    def __str__(self):
        return self.nome
