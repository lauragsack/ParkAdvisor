# Generated by Django 3.0.5 on 2020-04-13 19:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20200413_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='park_rating',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
