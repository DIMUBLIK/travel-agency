# Generated by Django 4.1.5 on 2023-01-16 16:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_alter_feedback_options_remove_feedback_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='score',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)], verbose_name='Оценка'),
        ),
    ]
