# Generated by Django 3.0.5 on 2020-04-13 19:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='category',
            field=models.CharField(choices=[('L', 'Lodging'), ('A', 'Activities'), ('F', 'Food')], default='Activities', max_length=1),
        ),
        migrations.AlterField(
            model_name='review',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='review',
            name='park_rating',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
