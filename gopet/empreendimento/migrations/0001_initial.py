# Generated by Django 2.0.3 on 2018-03-23 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empreendimento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email do responsável', models.CharField(max_length=30)),
                ('CNPJ', models.CharField(max_length=15)),
                ('Nome da empresa', models.CharField(max_length=50)),
                ('Segmentação/ Area de atuação', models.CharField(max_length=50)),
                ('Nome do proprietário', models.CharField(max_length=50)),
                ('Informações adicionais', models.TextField()),
                ('Hora do atendimento', models.TimeField()),
                ('Tipo do Serviço', models.CharField(max_length=50)),
                ('Ano de abertura', models.CharField(max_length=4)),
                ('Contato de emergência', models.CharField(max_length=50)),
            ],
        ),
    ]
