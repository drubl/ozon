# Generated by Django 3.0.5 on 2020-04-09 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basket', '0002_auto_20200408_1455'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basket',
            name='totalPrice',
        ),
        migrations.AddField(
            model_name='order',
            name='totalPrice',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Цена'),
        ),
    ]
