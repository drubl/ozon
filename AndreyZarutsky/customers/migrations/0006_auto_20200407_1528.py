# Generated by Django 3.0.5 on 2020-04-07 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0005_remove_customer_password'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'verbose_name_plural': 'Клиенты'},
        ),
    ]
