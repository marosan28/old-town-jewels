# Generated by Django 3.2.16 on 2023-02-14 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20230121_2043'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='payment_intent_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
