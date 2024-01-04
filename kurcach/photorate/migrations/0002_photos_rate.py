# Generated by Django 4.2.7 on 2023-12-27 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photorate', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photos',
            name='rate',
            field=models.IntegerField(choices=[(1, 'Poor'), (2, 'Average'), (3, 'Good'), (4, 'Very Good'), (5, 'Excellent')], default=1, verbose_name='Оценка'),
        ),
    ]
