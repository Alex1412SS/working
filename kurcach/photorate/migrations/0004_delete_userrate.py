# Generated by Django 4.2.7 on 2023-12-29 18:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photorate', '0003_userrate'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserRate',
        ),
    ]
