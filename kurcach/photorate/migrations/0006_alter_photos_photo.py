# Generated by Django 4.2.7 on 2023-12-29 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photorate', '0005_alter_photos_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photos',
            name='photo',
            field=models.ImageField(default=None, null=True, upload_to='media', verbose_name='Фото'),
        ),
    ]
