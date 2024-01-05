# Generated by Django 5.0 on 2023-12-23 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atores', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ator',
            name='nacionalidade',
            field=models.CharField(blank=True, choices=[('EUA', 'Estados Unidos'), ('BRA', 'Brasil'), ('ING', 'Inglaterra'), ('ARG', 'Argentina'), ('GER', 'Alemanha'), ('AUS', 'Austrália'), ('HOL', 'Holanda')], max_length=100, null=True),
        ),
    ]