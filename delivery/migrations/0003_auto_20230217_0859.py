# Generated by Django 3.2.16 on 2023-02-17 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0002_auto_20230215_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deliveryoption',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='deliveryoption',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
    ]