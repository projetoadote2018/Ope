from django.db import models

# Create your models here.

class Animal(models.Model):
    nome = models.CharField(max_length=50)
    ra = models.IntegerField()
    '''raca poderia ser uma FK'''
    raca = models.CharField(max_length=25)
    idade = models.IntegerField()
    portes = (
        ('pp', 'Muito pequeno'),
        ('p', 'Pequeno'),
        ('m', 'Medio'),
        ('g', 'Grande'),
        ('gg', 'Muito grande'),
    )
    porte = models.CharField(max_length=10, choices=portes)
    sexo = (
        ('Masculino', 'Masculino'),
        ('Feminino', 'Feminino'),
        ('Indefinido', 'Indefinido')
    )
    sexo = models.CharField(max_length=10, choices=sexo)
    castrado = models.BooleanField(default=False)
    origem = models.CharField(max_length=30)
    comport = models.CharField(max_length=30, name='Comportamento')
    saude = models.TextField(max_length=600, name='Descrição da saúde do animal')

    def __str__(self):
        return self.nome


class Adocao(models.Model):
    usuario = models.ForeignKey('usuarios.Usuario', name='Nome do usuário',on_delete=models.CASCADE)
    animal = models.ForeignKey('Animal', name='Animal a ser adotado',on_delete=models.CASCADE)
    data = models.DateField(name='Data da adoção')
    hora = models.TimeField(name='Hora da doação')
    contrato = models.CharField(max_length=15, name='Contrato de adoção')
    def __str__(self):
        return self.nome