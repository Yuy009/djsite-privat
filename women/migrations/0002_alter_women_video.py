# Generated by Django 5.0 on 2024-05-10 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='women',
            name='video',
            field=models.FileField(default='media/video.mp4', null=True, upload_to='media', verbose_name='Video'),
        ),
    ]
