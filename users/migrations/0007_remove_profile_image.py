# Generated by Django 3.2.16 on 2023-02-25 18:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_profile_alt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='image',
        ),
    ]
