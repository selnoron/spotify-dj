# Generated by Django 4.2.2 on 2023-07-14 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_song_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='audio_file',
            field=models.FileField(upload_to='songs/%Y/%m/%d/', verbose_name='аудио файл'),
        ),
    ]
