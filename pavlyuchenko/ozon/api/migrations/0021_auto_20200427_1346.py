# Generated by Django 3.0.5 on 2020-04-27 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0020_product_final_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='final_price',
        ),
        migrations.AddField(
            model_name='product',
            name='old_price',
            field=models.IntegerField(default=1300),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(blank=True),
        ),
    ]