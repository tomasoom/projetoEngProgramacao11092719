# Generated by Django 4.0.3 on 2022-05-02 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leagueTables', '0002_liga_nome_alter_clube_derrotas_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='clube',
            name='nacionalidade',
            field=models.CharField(default='Portuguesa', editable=False, max_length=30),
        ),
    ]
