# Generated by Django 5.0 on 2024-12-28 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='filme',
            name='capa',
            field=models.ImageField(blank=True, default='./no-photo.jpg', null=True, upload_to='capa_filmes/'),
        ),
    ]
