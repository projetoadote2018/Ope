from django.db import models

# Create your models here.
class Empreendimento (models.Model):
    email = models.CharField(max_length=30, name='Email do responsável')
    cnpj = models.CharField(max_length=15, name='CNPJ')
    nome = models.CharField(max_length=50, name='Nome da empresa')
    tipo = models.CharField(max_length=50, name='Segmentação/ Area de atuação')
    tipo_servico = models.CharField(max_length=50, name='Tipo do Serviço')
    nome_proprietario= models.CharField(max_length=50, name='Nome do proprietário')
    adcnl_info = models.TextField(name='Informações adicionais')
    hora_atend = models.TimeField(name='Hora do atendimento')
    tipo_servico = models.CharField(max_length=50, name='Tipo do Serviço')
    ano_abertura = models.CharField(max_length=4, name='Ano de abertura')
    atnd_emergencia = models.CharField(max_length=50, name='Contato de emergência')
    def __str__(self):
        return self.nome