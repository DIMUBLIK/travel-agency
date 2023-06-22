# Generated by Django 4.1.5 on 2023-01-16 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Applications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50, verbose_name='Имя клиента')),
                ('Place', models.CharField(max_length=50, verbose_name='Место путешествия')),
                ('PersonsCount', models.IntegerField(verbose_name='Количество людей')),
                ('days', models.IntegerField(verbose_name='Количество дней')),
                ('budget', models.IntegerField(verbose_name='Бюджет')),
                ('text', models.TextField(verbose_name='Пожелания')),
            ],
            options={
                'verbose_name': 'Заявка',
                'verbose_name_plural': 'Заявки',
            },
        ),
    ]
