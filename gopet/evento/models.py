from django.db import models

# Create your models here.
class Evento (models.Model):
    nome = models.CharField(max_length=40 , name='Nomde do Evento')
    descricao = models.TextField(max_length=70, name='Descrição')
    data = models.DateField(name='Data do evento')
    status = models.CharField(max_length=20, name='Status')
    hora = models.TimeField(name='Hora')
    def __str__(self):
        return self.nome