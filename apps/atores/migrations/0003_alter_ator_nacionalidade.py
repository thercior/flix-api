# Generated by Django 5.0 on 2024-02-12 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atores', '0002_alter_ator_nacionalidade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ator',
            name='nacionalidade',
            field=models.CharField(blank=True, choices=[('EUA', 'Estados Unidos'), ('BRA', 'Brasil'), ('ING', 'Inglaterra'), ('ARG', 'Argentina'), ('GER', 'Alemanha'), ('AUS', 'Austrália'), ('HOL', 'Holanda'), ('ESP', 'Espanha')], max_length=100, null=True),
        ),
    ]
