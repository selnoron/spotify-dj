# Generated by Django 4.2.2 on 2023-07-14 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_genre_song'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='duration',
            field=models.PositiveSmallIntegerField(verbose_name='длительность трека'),
        ),
    ]
