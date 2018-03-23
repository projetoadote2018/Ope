from django.db import models

# Create your models here.
class Usuario(models.Model):
    nome = models.CharField(max_length=30, name='Nome do usuario')
    cpf = models.CharField(max_length=14, name='CPF')
    email = models.CharField(max_length=30, name='E-mail')
    logradouro =models.CharField(max_length=50, name='Logradouro')
    numero = models.CharField(max_length=5, name='Numero')
    bairro = models.CharField(max_length=40, name='Bairro')
    complemento = models.CharField(max_length=40, name='Complemento')
    cidade = models.CharField(max_length=40, name='Cidade')

    estados ={
        ('Acre' ,'AC'),
        ('Alagoas', 'AL'),
        ('Amapá','AP'),
        ('Amazonas','AM'),
        ('Bahia','BA'),
        ('Ceará','CE'),
        ('Distrito Federal','DF'),
        ('Espírito Santo','ES'),
        ('Goiás','GO'),
        ('Maranhão','MA'),
        ('Mato Grosso','MT'),
        ('Mato Grosso do Sul', 'MS'),
        ('Minas Gerais','MG'),
        ('Pará','PA'),
        ('Paraíba','PB'),
        ('Paraná','PR'),
        ('Pernambuco','PE'),
        ('Piauí','PI'),
        ('Rio de Janeiro','RJ'),
        ('Rio Grande do Norte','RN'),
        ('Rio Grande do Sul','RS'),
        ('Rondônia','RO'),
        ('Roraima','RR'),
        ('Santa Catarina','SC'),
        ('São Paulo','SP'),
        ('Sergipe','SE'),
        ('Tocantins','TO')
    }
    estado = models.CharField(max_length=20, choices=estados)
    referencia = models.CharField(max_length=100, name='Ponto de referência')