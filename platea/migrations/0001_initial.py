# Generated by Django 4.2.17 on 2024-12-14 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExchangeRate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency_from', models.CharField(choices=[('USD', 'Dólar Estadounidense'), ('USDT', 'USDT'), ('PEN', 'Nuevo Sol Peruano')], max_length=4)),
                ('currency_to', models.CharField(choices=[('USD', 'Dólar Estadounidense'), ('USDT', 'USDT'), ('PEN', 'Nuevo Sol Peruano')], max_length=4)),
                ('rate', models.DecimalField(decimal_places=3, max_digits=10)),
            ],
        ),
    ]
