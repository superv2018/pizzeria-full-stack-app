# Generated by Django 4.1.5 on 2023-01-06 07:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizzeria',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='pizzeria',
            name='logo_image',
            field=models.ImageField(blank=True, default='pizzariaImages/pizzalogo.png', upload_to='pizzariaImages'),
        ),
        migrations.AddField(
            model_name='pizzeria',
            name='phone_number',
            field=models.CharField(blank=True, max_length=10, validators=[django.core.validators.RegexValidator(regex='^\\1?\\d{9, 10}$')]),
        ),
    ]
