# Generated by Django 3.0.5 on 2020-04-14 15:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0013_auto_20200413_1306'),
        ('basket', '0009_basket_totalcount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basket',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='customers.Customer'),
        ),
    ]
