# Generated by Django 3.0.5 on 2020-04-07 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20200407_0532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='firstPhoto',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='products',
            name='secondPhoto',
            field=models.CharField(default='', max_length=255),
        ),
    ]
