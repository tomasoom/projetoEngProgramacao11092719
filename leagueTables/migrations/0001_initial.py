# Generated by Django 4.0.3 on 2022-04-30 03:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clube',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('qualidade', models.IntegerField(default=50)),
                ('jogosDisputados', models.IntegerField(default=0)),
                ('vitorias', models.IntegerField(default=0)),
                ('empates', models.IntegerField(default=0)),
                ('derrotas', models.IntegerField(default=0)),
                ('golosMarcados', models.IntegerField(default=0)),
                ('golosSofridos', models.IntegerField(default=0)),
                ('diferencaDeGolos', models.IntegerField(default=0)),
                ('pontos', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Liga',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('listaEquipas', models.ManyToManyField(to='leagueTables.clube')),
            ],
        ),
        migrations.CreateModel(
            name='Jogo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('golosCasa', models.IntegerField(default=0)),
                ('golosFora', models.IntegerField(default=0)),
                ('equipaCasa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='equipaCasa', to='leagueTables.clube')),
                ('equipaFora', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='equipaFora', to='leagueTables.clube')),
            ],
        ),
    ]
