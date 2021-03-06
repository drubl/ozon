# Generated by Django 3.0.5 on 2020-04-13 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20200409_1120'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='password',
        ),
        migrations.AlterField(
            model_name='cart',
            name='is_checkout',
            field=models.BooleanField(default=False, verbose_name='Оформлена'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='birthday',
            field=models.DateField(),
        ),
    ]
