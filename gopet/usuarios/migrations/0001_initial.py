# Generated by Django 2.0.3 on 2018-03-23 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nome do usuario', models.CharField(max_length=30)),
                ('CPF', models.CharField(max_length=14)),
                ('E-mail', models.CharField(max_length=30)),
                ('Logradouro', models.CharField(max_length=50)),
                ('Numero', models.CharField(max_length=5)),
                ('Bairro', models.CharField(max_length=40)),
                ('Complemento', models.CharField(max_length=40)),
                ('Cidade', models.CharField(max_length=40)),
                ('estado', models.CharField(choices=[('Pará', 'PA'), ('Maranhão', 'MA'), ('Ceará', 'CE'), ('Espírito Santo', 'ES'), ('Distrito Federal', 'DF'), ('Amazonas', 'AM'), ('Tocantins', 'TO'), ('Paraíba', 'PB'), ('Bahia', 'BA'), ('Paraná', 'PR'), ('Roraima', 'RR'), ('Pernambuco', 'PE'), ('Rondônia', 'RO'), ('Rio Grande do Norte', 'RN'), ('Goiás', 'GO'), ('Sergipe', 'SE'), ('Rio Grande do Sul', 'RS'), ('Piauí', 'PI'), ('São Paulo', 'SP'), ('Santa Catarina', 'SC'), ('Mato Grosso', 'MT'), ('Acre', 'AC'), ('Alagoas', 'AL'), ('Minas Gerais', 'MG'), ('Amapá', 'AP'), ('Rio de Janeiro', 'RJ'), ('Mato Grosso do Sul', 'MS')], max_length=20)),
                ('Ponto de referência', models.CharField(max_length=100)),
            ],
        ),
    ]
