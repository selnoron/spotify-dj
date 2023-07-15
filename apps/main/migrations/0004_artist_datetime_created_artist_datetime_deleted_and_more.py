# Generated by Django 4.2.2 on 2023-07-05 14:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_artist_band_alter_artist_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='datetime_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='дата создания'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='artist',
            name='datetime_deleted',
            field=models.DateTimeField(blank=True, null=True, verbose_name='дата удаления'),
        ),
        migrations.AddField(
            model_name='artist',
            name='datetime_updated',
            field=models.DateTimeField(auto_now=True, verbose_name='дата обновления'),
        ),
    ]
