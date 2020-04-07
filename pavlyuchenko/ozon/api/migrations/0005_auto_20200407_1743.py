# Generated by Django 3.0.5 on 2020-04-07 14:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20200407_1740'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='customer',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='api.Customer'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cart',
            name='is_checkout',
            field=models.BooleanField(default=False, verbose_name='Оформлена'),
            preserve_default=False,
        ),
    ]
