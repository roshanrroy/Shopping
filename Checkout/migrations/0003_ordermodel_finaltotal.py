# Generated by Django 5.1 on 2024-10-24 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Checkout', '0002_rename_city_ordermodel_city_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermodel',
            name='finaltotal',
            field=models.FloatField(default=None),
        ),
    ]
