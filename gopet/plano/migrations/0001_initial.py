# Generated by Django 2.0.3 on 2018-03-23 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Planos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_plano', models.CharField(max_length=25)),
                ('Preço', models.DecimalField(decimal_places=2, max_digits=9)),
                ('Nome', models.CharField(max_length=10)),
                ('Descrição', models.CharField(max_length=100)),
                ('Forma de pagamento', models.CharField(max_length=20)),
            ],
        ),
    ]
