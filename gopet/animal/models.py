from django.db import models

# Create your models here.

class Categoria(models.Model):
    nome_categoria = models.CharField(max_length=25, null=False, blank=False)
    def __str__(self):
        return self.nome


class Especie(models.Model):
    nome_especie = models.CharField(max_length=50, null=False)
    def __str__(self):
        return self.nome


class Animal(models.Model):
    nome_animal = models.CharField(max_length=50)
    especie = models.ForeignKey(Especie, on_delete=models.CASCADE)
    raca = models.CharField(max_length=25)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    portes = (
        ('pp', 'Muito pequeno'),
        ('p', 'Pequeno'),
        ('m', 'Medio'),
        ('g', 'Grande'),
        ('gg', 'Muito grande'),
    )
    porte = models.CharField(max_length=10, choices=portes)
    generos = (
        ('masc','Masculino'),
        ('fem', 'Feminino'),
    )
    genero = models.CharField(max_length=5, choices=generos)
    ra = models.CharField(max_length=10, null=False)
    status = models.CharField(max_length=10, null=True)
    img = models.CharField(max_length=10000, null=True)
    restricao_doacao = models.BooleanField(default=False)
    saude = models.CharField(max_length=50, null=True)
    tipo = models.CharField(max_length=50, null=True)
    castracao = models.BooleanField(default=False)
    coleira = models.CharField(max_length=15, null=False)
    endereco = models.CharField(max_length=100 , default='Esse dado virá de outro app --provavel--', null=True)
    def __str__(self):
        return self.nome

